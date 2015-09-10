# coding=utf-8
from datetime import timedelta, date
import logging
from django.core.exceptions import FieldError
from django.utils.timezone import now

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.security import *

from fitAdmin.models import User, SportConf, SportDate, SportStat, SportDetail,Knowledge,KnowledgeType,Product,ProductPicture
from fitApi.serializers import *


@api_view(['GET', 'POST'])
def user_list(request, format=None):
    if request.method == 'GET':
        snippets = User.objects.all()
        serializer = UserSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def user_login(request):
    if request.method == 'GET':
        return Response(status=status.HTTP_403_FORBIDDEN)

    elif request.method == 'POST':
        try:
            request.DATA['android']
            login_type = 2  # android
        except KeyError:
            login_type = 0
        if not login_type:
            try:
                request.DATA['ios']
                login_type = 3  # ios
            except KeyError:
                login_type = 1  # web

        # if login_type == 1:
        #     return Response({'status': 0, 'message': '需传输终端字段'})

        try:
            loginname = request.DATA['loginname']
        except KeyError:
            return Response({'status': 0, 'message': 'loginname 帐号必须填写'})

        try:
            password = request.DATA['password']
        except KeyError:
            return Response({'status': 0, 'message': 'password 密码必须填写'})

        users = User.objects.filter(loginname=loginname)

        if not users.exists():
            return Response({'status': 0, 'message': '用户不存在'})
        else:
            user = users.first()
            # Y9VtcSMp3KQ=  123456

            if login_type != 1:  # 不是web才加密 web直接登录了
                password = desDecrypt(password)
            else:
                password = str(password)

            if user.password != md5(password):
                return Response({'status': 0, 'message': '密码不正确'})
            elif not user.is_active:
                return Response({'status': 0, 'message': '用户已锁定'})
            else:
                if request.META.has_key('HTTP_X_FORWARDED_FOR'):
                    ip = request.META['HTTP_X_FORWARDED_FOR']
                else:
                    ip = request.META['REMOTE_ADDR']

                user.last_login_time = datetime.now()
                user.last_login_ip = ip
                user.last_login_type = login_type
                user.login()

                token = tokenGenerate({"id": user.id, "name": user.loginname})

                return Response({'status': 1, 'message': '登录成功', 'data': token})


@api_view(['GET', 'POST'])
def user_profile(request):
    try:
        token = request.GET['t']
    except KeyError:
        return Response({'status': 1, 'message': 'token值不存在'})

    log = logging.getLogger('common')

    token_data = tokenParse(token)

    if not token_data:
        return Response({'status': 1, 'message': 'token值不正确'})

    uid = token_data['id']

    try:
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        return Response({'status': 1, 'message': 'token解析不出来'})

    if request.method == 'GET':
        serializer = UserSerializer(user)

        return Response(dict(status=0, message='ok', data=serializer.data))

    elif request.method == 'POST':
        try:
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(dict(status=0, message='ok'))

            return Response(dict(status=1, message=serializer.errors))
        except Exception as exc:
            return Response(dict(status=1, message=exc.detail))


@api_view(['POST', 'GET'])
def user_avatar(request):
    try:
        token = request.GET['t']
    except KeyError:
        return Response({'status': 1, 'message': 'token值不存在'})

    token_data = tokenParse(token)

    if not token_data:
        return Response({'status': 1, 'message': 'token值不正确'})

    uid = token_data['id']

    try:
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        return Response(dict(status=1, message='token解析不出来'))

    if request.method == 'GET':
        serializer = AvatarSerializer(user)
        avatar = serializer.data['avatar']
        return Response(dict(status=0, message='ok', data=avatar))

    elif request.method == 'POST':
        try:
            serializer = AvatarSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                avatar = serializer.data['avatar']
                return Response(dict(status=0, message='ok', data=avatar))

            return Response(dict(status=1, message=serializer.errors))
        except Exception as exc:
            return Response(dict(status=1, message=exc.detail))


@api_view(['GET', 'POST'])
def user_profile(request):
    try:
        token = request.GET['t']
    except KeyError:
        return Response({'status': 1, 'message': 'token值不存在'})

    log = logging.getLogger('common')

    token_data = tokenParse(token)

    if not token_data:
        return Response({'status': 1, 'message': 'token值不正确'})

    uid = token_data['id']

    try:
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        return Response({'status': 1, 'message': 'token解析不出来'})

    if request.method == 'GET':
        serializer = UserSerializer(user)

        return Response(dict(status=0, message='ok', data=serializer.data))

    elif request.method == 'POST':
        try:
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(dict(status=0, message='ok'))

            return Response(dict(status=1, message=serializer.errors))
        except Exception as exc:
            return Response(dict(status=1, message=exc.detail))


@api_view(['POST', 'GET'])
def sport_conf(request):
    try:
        token = request.GET['t']
    except KeyError:
        return Response({'status': 1, 'message': 'token值不存在'})

    token_data = tokenParse(token)

    if not token_data:
        return Response({'status': 1, 'message': 'token值不正确'})

    uid = token_data['id']

    try:
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        return Response(dict(status=1, message='token解析不出来'))

    if request.method == 'GET':
        try:
            sportConf = user.sportconf
        except SportConf.DoesNotExist:
            return Response(dict(status=1, message='未设置目标'))

        serializer = SportConfSerializer(sportConf)
        return Response(dict(status=0, message='ok', data=serializer.data))

    elif request.method == 'POST':
        '''
        如果没有设置目标的话，可以通过POST创建目标，首先初始化一个
        '''
        try:
            sportConf = user.sportconf
        except SportConf.DoesNotExist:
            user.sportconf = SportConf()
            sportConf = user.sportconf

        try:
            serializer = SportConfSerializer(sportConf, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(dict(status=0, message='ok', data=serializer.data))

            return Response(dict(status=1, message=serializer.errors))
        except Exception as exc:
            return Response(dict(status=1, message=exc.detail))


@api_view(['GET'])
def sport_stat(request):
    try:
        token = request.GET['t']
    except KeyError:
        return Response({'status': 1, 'message': 'token值不存在'})

    token_data = tokenParse(token)

    if not token_data:
        return Response({'status': 1, 'message': 'token值不正确'})

    uid = token_data['id']

    try:
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        return Response(dict(status=1, message='token解析不出来'))

    # 如果没有统计数据，肯定也没有明细的，所以可以直接返回了
    try:
        sportStat = user.sportstat
    except SportStat.DoesNotExist:
        user.sportstat = SportStat()
        user.sportstat.save()
        sportStat = user.sportstat

    today = now().date()

    sportDate = user.sportdate_set.filter(sport_date__exact=today).first()
    if not sportDate:
        sportDate = SportDate(user=user, sport_date=today)
        user.sportdate_set.add(sportDate)

    try:
        statSerializer = SportStatSerializer(sportStat)
        dateSerializer = SportDateSerializer(sportDate)
        return Response(dict(status=0, message='ok', data=dict(total=statSerializer.data, today=dateSerializer.data)))
    except Exception as exc:
        return Response(dict(status=1, message=exc.detail))


@api_view(['GET'])
def sport_date(request):
    try:
        token = request.GET['t']
    except KeyError:
        return Response({'status': 1, 'message': 'token值不存在'})

    token_data = tokenParse(token)

    if not token_data:
        return Response({'status': 1, 'message': 'token值不正确'})

    uid = token_data['id']

    try:
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        return Response(dict(status=1, message='token解析不出来'))

    sportDates = []
    try:
        start_str = request.GET['from']
    except KeyError:
        # 如果from参数为空，to也无用，默认返回今天的
        today = now().date()
        sportDates = user.sportdate_set.filter(sport_date__exact=today)

        if not sportDates:
            # 没有今天的数据，则初始化一个
            sportDate = SportDate(user=user, sport_date=today)
            user.sportdate_set.add(sportDate)
            sportDates = [sportDate]

    # 如果sportDates 没有数据，则表示存在 from 字段
    if not sportDates:
        try:
            start = datetime.datetime.strptime(start_str, '%Y-%m-%d')
        except ValueError:
            return Response(dict(status=1, message='from参数转为日期格式失败'))

        try:
            end_str = request.GET['to']
        except KeyError:
            # 如果没有to参数，则默认到今天
            end = now().date()
            end_str = now().strftime('%Y-%m-%d')

        if not end:  # 有to参数，转为日期
            try:
                end = datetime.datetime.strptime(end_str, '%Y-%m-%d').date()
            except ValueError:
                return Response(dict(status=1, message='to参数转为日期格式失败'))

        sportDates = user.sportdate_set.filter(sport_date__range=(start, end)).order_by('sport_date')

    if not sportDates:
        return Response(dict(status=1, message='时间段 ' + str(start_str) + ' 至 ' + str(end_str) + ' 没有运动数据，请确保时间段正确'))

    result_data = []
    for sportDate in sportDates:
        dateSerializer = SportDateSerializer(sportDate)
        result_data.append(dateSerializer.data)

    return Response(dict(status=0, message='ok', data=result_data))


'''
获取运动排名
t：token
type：排名类型 steps,points,distances,calories
'''


@api_view(['GET'])
def sport_rank(request):
    try:
        token = request.GET['t']
    except KeyError:
        return Response({'status': 1, 'message': 'token值不存在'})

    token_data = tokenParse(token)

    if not token_data:
        return Response({'status': 1, 'message': 'token值不正确'})

    uid = token_data['id']

    try:
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        return Response(dict(status=1, message='token解析不出来'))

    today = now().date()
    rank_type = 'steps'
    try:
        # 支持多种排序规则 steps,points,distances,calories, 默认是steps
        rank_type = request.GET['type']
    except KeyError:
        rank_type = 'steps'

    try:
        sportRanks = SportDate.objects.filter(sport_date__exact=today).order_by('-' + rank_type)[0:10];

        result_date = []
        rank = 1
        for sportRank in sportRanks:
            dateSerializer = SportDateSerializer(sportRank)
            userSerializer = UserBriefSerializer(sportRank.user)
            result_date.append(dict(rank=rank, sport=dateSerializer.data, user=userSerializer.data))
            rank += 1

        return Response(dict(status=0, message='ok', data=result_date))
    except FieldError:
        return Response(dict(status=1, message='排序字段只能是：steps,points,distances,calories'))
    except:
        return Response(dict(status=1, message='获取排名发生异常，请重试'))


'''
获取个人运动明细
t：token
type： steps,points,distances,calories
'''
@api_view(['GET'])
def sport_detail(request):
    try:
        token = request.GET['t']
    except KeyError:
        return Response({'status': 1, 'message': 'token值不存在'})

    token_data = tokenParse(token)

    if not token_data:
        return Response({'status': 1, 'message': 'token值不正确'})

    uid = token_data['id']

    try:
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        return Response(dict(status=1, message='token解析不出来'))

    sport_details = []
    try:
        start_str = request.GET['from']
    except KeyError:
        # 如果from参数为空，to也无用，默认返回今天的所有运动数据

        today_begin = time.strftime('%Y-%m-%d 0:0:0', time.localtime(time.time()))
        sport_details = user.sportdetail_set.filter(create_time__gte=today_begin).order_by('create_time')

        if not sport_details:
            # 没有今天的数据，则返回失败
            return Response(dict(status=1, message='今天还没开始运动'))

    # 说明form存在
    if not sport_details:
        try:
            start = datetime.datetime.strptime(start_str + ' 0:0:0', '%Y-%m-%d %H:%M:%S')
        except ValueError:
            return Response(dict(status=1, message='from参数转为日期格式失败'))

        try:
            end_str = request.GET['to']
        except KeyError:
            # 如果没有to参数，则默认到现在
            end = datetime.now()
            end_str = end.strftime("%Y-%m-%d")

        if not end:  # 有to参数，转为日期
            try:
                end = datetime.datetime.strptime(end_str + ' 23:59:59', '%Y-%m-%d %H:%M:%S')
            except ValueError:
                return Response(dict(status=1, message='to参数转为日期格式失败'))

        if start > end:
            return Response(
                dict(status=1, message='开始时间: ' + str(start_str) + ' 大于 结束时间: ' + str(end_str) + ' ，请确保时间段正确'))

        sport_details = user.sportdetail_set.filter(create_time__range=(start, end)).order_by('create_time')

    if not sport_details:
        return Response(dict(status=1, message='时间段 ' + str(start_str) + ' 至 ' + str(end_str) + ' 没有运动数据，请确保时间段正确'))

    result_data = []
    for sport__detail in sport_details:
        detail_serializer = SportDetailSerializer(sport__detail)
        result_data.append(detail_serializer.data)

    return Response(dict(status=0, message='ok', data=result_data))

'''
健康宣教未读数量
    最新的，但是未查看的知识

'''
# TODO 是否需要验证呢？
@api_view(['GET'])
def knowledge_new_count(request):
    try:
        token = request.GET['t']
    except KeyError:
        return Response({'status': 1, 'message': 'token值不存在'})

    token_data = tokenParse(token)

    if not token_data:
        return Response({'status': 1, 'message': 'token值不正确'})

    # uid = token_data['id']
    #
    # try:
    #     user = User.objects.get(pk=uid)
    # except User.DoesNotExist:
    #     return Response(dict(status=1, message='token解析不出来'))

    new_count = 0
    from_str = request.GET.get('from',1)

    # 必须要传个from参数 时间
    if from_str == 1:
        return Response(dict(status=1, message='from参数不能为空，必须是日期格式，格式必须是 yyyy-mm-dd HH:mm:ss'))

    try:
        from_time = datetime.datetime.strptime(from_str, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return Response(dict(status=1, message='from参数转为日期格式失败，格式必须是 yyyy-mm-dd HH:mm:ss'))

    no_read = Knowledge.objects.filter(create_time__gte=from_time).count()

    return Response(dict(status=0, message='ok', data=no_read))

'''
健康宣教 获取列表

如果有from参数
    则从from开始的所有
如果没有from参数
    获取最新的20条
'''
# TODO 是否需要验证呢？

@api_view(['GET'])
def knowledge_list(request):
    try:
        token = request.GET['t']
    except KeyError:
        return Response({'status': 1, 'message': 'token值不存在'})

    token_data = tokenParse(token)

    if not token_data:
        return Response({'status': 1, 'message': 'token值不正确'})

    # uid = token_data['id']
    #
    # try:
    #     user = User.objects.get(pk=uid)
    # except User.DoesNotExist:
    #     return Response(dict(status=1, message='token解析不出来'))

    from_str = request.GET.get('from',0)

    if from_str == 0:
        # 没有from参数 一般是第一次获取 返回最近10天的知识
        from_time = date.today()-timedelta(days=10)
    else:
        try:
            from_time = datetime.datetime.strptime(from_str, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            return Response(dict(status=1, message='from参数转为日期格式失败，格式必须是 yyyy-mm-dd HH:mm:ss'))

    knowledgelist = Knowledge.objects.filter(create_time__gte=from_time).order_by('-create_time')

    result_data = []
    for knowledge_item in knowledgelist:
        #前100个字符
        knowledge_item.content = knowledge_item.content[0:100]
        knowledge_item_serializer = KnowledgeSerializer(knowledge_item)

        #获取类型对象 可能多个嘛
        knowledge_item_types = knowledge_item.types.all()
        knowledge_type_data = []
        for knowledge_item_type in knowledge_item_types:
            knowledge_type_data.append(KnowledgeTypeSerializer(knowledge_item_type).data)

        result_data.append(dict(knowledge=knowledge_item_serializer.data, types=knowledge_type_data))

    return Response(dict(status=0, message='ok', data=result_data))


'''
健康宣教 获取列表 某个类型的知识
'''
# TODO 是否需要验证呢？

@api_view(['GET'])
def knowledge_type_list(request):
    try:
        token = request.GET['t']
    except KeyError:
        return Response({'status': 1, 'message': 'token值不存在'})

    token_data = tokenParse(token)

    if not token_data:
        return Response({'status': 1, 'message': 'token值不正确'})

    # uid = token_data['id']
    #
    # try:
    #     user = User.objects.get(pk=uid)
    # except User.DoesNotExist:
    #     return Response(dict(status=1, message='token解析不出来'))

    l_type = request.GET.get('type',0)
    if l_type == 0:
        return Response(dict(status=1, message='type参数是必须的，且必须是Int类型'))
    l_type = int(l_type)
    if type(l_type) != int:
        return Response(dict(status=1, message='type参数必须是Int类型'))

    page = request.GET.get('page',1)
    page = int(page)
    if page < 1:
        page = 1;

    if type(page) != int:
        return Response(dict(status=1, message='page参数是必须的，必须是Int类型'))

    index_begin = (page-1)*20
    index_end = index_begin+20

    knowledge_type = KnowledgeType.objects.get(id=l_type)
    if not knowledge_type:
        return Response(dict(status=1, message='type参数:'+l_type+'，对应的类型不存在'))

    knowledgelist = knowledge_type.knowledge_set.all().order_by('-create_time')[index_begin:index_end]

    result_data = []
    for knowledge_item in knowledgelist:
        #前100个字符
        knowledge_item.content = knowledge_item.content[0:100]
        knowledge_item_serializer = KnowledgeSerializer(knowledge_item)

        result_data.append(knowledge_item_serializer.data)

    return Response(dict(status=0, message='ok', data=result_data))


'''
健康宣教 获取明细

'''
# TODO 是否需要验证呢？

@api_view(['GET'])
def knowledge_detail(request):
    try:
        token = request.GET['t']
    except KeyError:
        return Response({'status': 1, 'message': 'token值不存在'})

    token_data = tokenParse(token)

    if not token_data:
        return Response({'status': 1, 'message': 'token值不正确'})

    # uid = token_data['id']
    #
    # try:
    #     user = User.objects.get(pk=uid)
    # except User.DoesNotExist:
    #     return Response(dict(status=1, message='token解析不出来'))

    id = request.GET.get('id',0)

    if id == 0:
        # 必须得有id参数
        return Response(dict(status=1, message='id参数不能为空'))
    else:
        knowledge_item = Knowledge.objects.get(pk=id)

        knowledge_item.read_count+=1
        knowledge_serializer = KnowledgeSerializer(knowledge_item)

        #获取类型对象 可能多个嘛
        knowledge_types = knowledge_item.types.all()
        knowledge_type_data = []
        for knowledge_type in knowledge_types:
            knowledge_type_data.append(KnowledgeTypeSerializer(knowledge_type).data)

        knowledge_item.save()
        return Response(dict(status=0, message='ok', data=(dict(knowledge=knowledge_serializer.data, types=knowledge_type_data))))


'''
获取商品列表
    没有具体验证是某个人来获取的
    pz 每页获取的大小 默认20
    page 页数 数字
    order 排序字段 price：价格  new：新鲜程度（默认）  discount：折扣
    ot 排序类型 1：顺序（默认）  0：逆序
    key 查询关键字
'''
@api_view(['GET'])
def product_list(request):
    try:
        token = request.GET['t']
    except KeyError:
        return Response({'status': 1, 'message': 'token值不存在'})

    token_data = tokenParse(token)

    if not token_data:
        return Response({'status': 1, 'message': 'token值不正确'})

    # uid = token_data['id']
    #
    # try:
    #     user = User.objects.get(pk=uid)
    # except User.DoesNotExist:
    #     return Response(dict(status=1, message='token解析不出来'))

    #如果没有默认20，如果是非数字 默认20
    pz = request.GET.get('pz',20)
    pagesize = int(pz)
    if type(pagesize) != int:
      pagesize = 20

    #
    page = request.GET.get('page', 1)
    page = int(page)
    if page < 1:
        page = 1

    index_begin = (page-1)*pagesize
    index_end = index_begin+pagesize

    if type(page) != int:
        return Response(dict(status=1, message='page参数必须是Int类型'))

    order_str = ""
    order_type = request.GET.get('ot', "1")
    if order_type == "0":
        order_str = "-"

    order_field = request.GET.get('order', 'create_time')

    order_fields = ["create_time", "discount", "price", "cell_count"]
    if order_field not in order_fields:
        return Response(dict(status=1, message='order参数不正确'))

    order_str += order_field

    key = request.GET.get('key','')

    product_data = []
    if key:
        #此处不能用 contains，因为要支持中文嘛 'contains': 'LIKE BINARY %s', 'icontains': 'LIKE %s'
        product_data = Product.objects.filter(is_delete=0).filter(name__icontains=key).order_by(order_str)[index_begin:index_end]
    else:
        product_data = Product.objects.filter(is_delete=0).order_by(order_str)[index_begin:index_end]

    result_data = []
    for product_item in product_data:
        product_item_picture = product_item.productpicture_set.order_by('seq').first()
        if product_item_picture:
            product_item.picture = product_item_picture.pic_path
        else:
            #第一个是默认图片 需要初始化
            product_item.picture = ProductPicture.objects.get(pk=1)
        product_item_serializer = ProductBriefSerializer(product_item)

        result_data.append(product_item_serializer.data)

    return Response(dict(status=0, message='ok', data=result_data))


'''
获取某个商品的明细
    没有具体验证是某个人来获取的
    id 商品的id
'''
@api_view(['GET'])
def product_detail(request):
    try:
        token = request.GET['t']
    except KeyError:
        return Response({'status': 1, 'message': 'token值不存在'})

    token_data = tokenParse(token)

    if not token_data:
        return Response({'status': 1, 'message': 'token值不正确'})

    # uid = token_data['id']
    #
    # try:
    #     user = User.objects.get(pk=uid)
    # except User.DoesNotExist:
    #     return Response(dict(status=1, message='token解析不出来'))

    id = request.GET.get('id',0)

    if id == 0:
        # 必须得有id参数
        return Response(dict(status=1, message='id参数不能为空'))
    else:
        product_item = Product.objects.get(pk=id)

        product_item.read_count+=1

        #获取类型对象 可能多个嘛
        product_pics = product_item.productpicture_set.filter(is_delete=0).order_by("seq")
        product_pics_data = []
        for product_pic in product_pics:
            #直接获取pic_path 没有把/media父级文件夹名称加上，所以还是序列化下吧
            product_pics_data.append(ProductPictureSerializer(product_pic).data.get('picture'))

        if not product_pics_data:
            # 数据库第一个存的是没有默认图片
            product_pic = ProductPicture.objects.get(pk=1)
            product_pics_data.append(ProductPictureSerializer(product_pic).data.get('picture'))

        product_item.pictures = product_pics_data
        product_serializer = ProductSerializer(product_item)

        #保存查看+1
        product_item.save()
        return Response(dict(status=0, message='ok', data=product_serializer.data))

'''
    提交订单
        [{product_id,order_price,number,total}]
'''
# TODO 待开发
@api_view(['GET','POST'])
def order_buy(request):
    try:
        token = request.GET['t']
    except KeyError:
        return Response({'status': 1, 'message': 'token值不存在'})

    token_data = tokenParse(token)

    if not token_data:
        return Response({'status': 1, 'message': 'token值不正确'})

    uid = token_data['id']

    try:
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        return Response(dict(status=1, message='token解析不出来'))

    if request.method == 'GET':
        try:
            order = user.order_set.get(pk=1)
            if not order:
                return Response(dict(status=1, message='没有该订单'))

            order_details = order.orderdetail_set.all()

            result_data = []
            for order_detail in order_details:
                order_detail_serializer = OrderBuySerializer(order_detail)
                result_data.append(order_detail_serializer.data)

            return Response(result_data)
        except SportConf.DoesNotExist:
            return Response(dict(status=1, message='未设置目标'))

    elif request.method == 'POST':
        try:
            sportConf = user.sportconf
        except SportConf.DoesNotExist:
            user.sportconf = SportConf()
            sportConf = user.sportconf

        try:
            serializer = SportConfSerializer(sportConf, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(dict(status=0, message='ok', data=serializer.data))

            return Response(dict(status=1, message=serializer.errors))
        except Exception as exc:
            return Response(dict(status=1, message=exc.detail))


'''
查询订单列表
    pz 每页获取的大小 默认20
    page 页数 数字

    默认订单创建日期按照日期从新到旧

    from 查询开始日期
    to 查询结束日期
'''
@api_view(['GET'])
def order_list(request):
    try:
        token = request.GET['t']
    except KeyError:
        return Response({'status': 1, 'message': 'token值不存在'})

    token_data = tokenParse(token)

    if not token_data:
        return Response({'status': 1, 'message': 'token值不正确'})

    uid = token_data['id']

    try:
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        return Response(dict(status=1, message='token解析不出来'))

    #如果没有默认20，如果是非数字 默认20
    pz = request.GET.get('pz',20)
    pagesize = int(pz)
    if type(pagesize) != int:
      pagesize = 20

    page = request.GET.get('page', 1)
    page = int(page)
    if page < 1:
        page = 1

    index_begin = (page-1)*pagesize
    index_end = index_begin+pagesize

    start_str = request.GET.get('from','0')
    end_str = request.GET.get('to','0')

    #即没有查询条件
    if start_str+end_str == '00':
        orderList = user.order_set.all().order_by('-create_time')[index_begin:index_end]
    else:
        try:
            start = datetime.datetime.strptime(start_str, '%Y-%m-%d')
            end = datetime.datetime.strptime(end_str, '%Y-%m-%d')
        except ValueError:
            return Response(dict(status=1, message='from 或 to 参数转为日期格式失败，必须是形如: 2015-09-11 01:40:00'))

        orderList = user.order_set.filter(create_time__range=(start, end)).order_by('-create_time')[index_begin:index_end]

    # 处理订单列表 把订单的明细也要一起传回去
    # TODO 此处没有考虑 已卖出商品的 历史记录，以后再考虑吧
    # 也没有考虑订单商品对象 和 原始对象的不同 直接把orderDetail扩展了几个字段

    result_data = []
    for order in orderList:
        order_details = order.orderdetail_set.all()

        order_product_data = []
        for order_detail in order_details:
            product_pic = order_detail.product.productpicture_set.first()
            if not product_pic:
                # 数据库第一个存的是没有默认图片
                product_pic = ProductPicture.objects.get(pk=1)
            #图片
            product_pic = ProductPictureSerializer(product_pic).data.get('picture')

            #名称
            product_name = order_detail.product.name

            #订单里面的一个商品
            order_product_serializer = dict(id=order_detail.product_id,name=product_name, picture=product_pic,\
                                            number=order_detail.number,total = order_detail.total,\
                                            order_price=order_detail.order_price,\
                                            product_price=order_detail.order_price)

            order_product_data.append(order_product_serializer)

        order_status = order.get_status_display()
        result_data.append(dict(id=order.id,code=order.order_code,total=order.total_pay,status=order_status,create_time=order.create_time,products=order_product_data))

    return Response(dict(status=0,message='ok',data=result_data))


'''
查询订单详情
    id 订单id

    显示订单的处理流程 operLog
'''
@api_view(['GET'])
def order_detail(request):
    try:
        token = request.GET['t']
    except KeyError:
        return Response({'status': 1, 'message': 'token值不存在'})

    token_data = tokenParse(token)

    if not token_data:
        return Response({'status': 1, 'message': 'token值不正确'})

    uid = token_data['id']

    try:
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        return Response(dict(status=1, message='token解析不出来'))

    id = request.GET.get('id',0)

    if id == 0:
        # 必须得有id参数
        return Response(dict(status=1, message='id参数不能为空'))
    else:
        order_item = Order.objects.get(pk=id)

        #获取订单的商品明细
        order_details = order_item.orderdetail_set.all().order_by('product_id')
        order_product_data = []
        for order_detail in order_details:
            product_pic = order_detail.product.productpicture_set.first()
            if not product_pic:
                # 数据库第一个存的是没有默认图片
                product_pic = ProductPicture.objects.get(pk=1)
            #图片
            product_pic = ProductPictureSerializer(product_pic).data.get('picture')

            #名称
            product_name = order_detail.product.name

            #订单里面的一个商品
            order_product_serializer = dict(id=order_detail.product_id,name=product_name, picture=product_pic,\
                                            number=order_detail.number,total = order_detail.total,\
                                            order_price=order_detail.order_price,\
                                            product_price=order_detail.order_price)

            order_product_data.append(order_product_serializer)

        #获取订单的操作明细
        order_logs = order_item.orderoperlog_set.all().order_by("action_time")
        order_logs_data = []
        for order_log in order_logs:

            order_log_item = dict(name=order_log.actor.realname,time = order_log.action_time,action=order_log.action)

            order_logs_data.append(order_log_item)

        order_status = order_item.get_status_display()

        result_data = dict(id=order_item.id,code=order_item.order_code,total=order_item.total_pay,\
                           status=order_status,create_time=order_item.create_time,products=order_product_data,logs=order_logs_data)
    return Response(dict(status=0,message='ok',data=result_data))



