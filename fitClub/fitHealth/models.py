# coding=utf-8
import hashlib
from django.db import models

sex_choices = (
    (1, '男'),
    (2, '女'),
)

login_type_choices = (
    (1, 'Web'),
    (2, 'Android'),
    (3, 'iOS'),
)

device_status_choices = (
    (1, '激活'),
    (2, '丢失'),
    (3, '其他'),
)

alarm_type_choices = (
    (101, '步数'),
    (102, '公里数'),
    (103, '点数'),
    (104, '卡路里'),
    (201, '睡眠'),
    (202, '体重'),
    (203, '血压'),
)

alarm_channel_choices = (
    (1,"应用"),
    (2,"微信"),
    (3,"短信"),
    (4,"邮件"),
)

order_status_choices = (
    (1, '已下单'),
    (2, '已确认'),
    (3, '已发货'),
    (4, '已收货'),
)


class User(models.Model):
    loginname = models.CharField(max_length=20, unique=True, null=False)
    password = models.CharField(max_length=20, null=False)
    nickname = models.CharField(max_length=20, null=True)
    realname = models.CharField(max_length=20)
    sex = models.IntegerField(choices=sex_choices)
    age = models.IntegerField(null=True)
    birthday = models.DateField()
    company = models.CharField(max_length=50, null=True)
    job = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=100, null=True)
    weixin = models.CharField(max_length=20, null=True)
    qq = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=30, null=True)
    identity = models.CharField(max_length=18, null=True)
    create_time = models.DateTimeField()
    create_by = models.IntegerField()
    is_active = models.BooleanField()
    last_login_time = models.DateTimeField(null=True)
    last_login_ip = models.CharField(max_length=40, null=True)
    last_login_type = models.IntegerField(choices=login_type_choices)

    def __unicode__(self):
        return self.loginname

    def save(self, *args, **kwargs): #默认的，给后台admin用的
        self.password = hashlib.sha1(self.password).hexdigest()
        super(User, self).save(*args, **kwargs)

    def login(self,*args, **kwargs): #平时就用这个，密码不修改
        super(User, self).save(*args, **kwargs)


class MemberLevel(models.Model):
    name = models.CharField(max_length=20)
    descriptipn = models.CharField(max_length=200, null=True)

    def __unicode__(self):
        return self.name

class Member(models.Model):
    user = models.ForeignKey(User)
    join_date = models.DateField()
    end_date = models.DateField()
    level = models.ForeignKey(MemberLevel, null=True)

    def __unicode__(self):
        return self.user.loginname

# 设备厂商
class DeviceBrand(models.Model):
    name = models.CharField(max_length=20, unique=True)
    desc = models.CharField(max_length=200, null=True)

    def __unicode__(self):
        return self.name

# 设备
class Device(models.Model):
    name = models.CharField(max_length=10, unique=True)
    brand = models.ForeignKey(DeviceBrand)
    mac = models.CharField(max_length=30, null=True)
    device_user = models.CharField(max_length=20)
    device_token = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

# 用户设备
class DeviceUser(models.Model):
    user = models.ForeignKey(User)
    device = models.ForeignKey(Device)
    bind_time = models.DateField()
    status = models.IntegerField(choices=device_status_choices)

# 体重记录
class HealthWeight(models.Model):
    user = models.ForeignKey(User)
    date = models.DateTimeField()
    weight = models.FloatField(default=0)

# 血压记录
class HealthBloodPress(models.Model):
    user = models.ForeignKey(User)
    date = models.DateTimeField()
    low_pressure = models.FloatField()
    high_pressure = models.FloatField()

# 睡眠记录
class HealthSleep(models.Model):
    user = models.ForeignKey(User)
    begin_time = models.DateTimeField()
    auto_detected = models.BooleanField()
    duration = models.IntegerField(null=True)
    details = models.CharField(max_length=500, null=True)

# 运动记录
class Sport(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField()
    points = models.IntegerField()
    steps = models.IntegerField(null=True)
    calories = models.FloatField(max_length=9, null=True)
    distance = models.FloatField(max_length=9)

# 运动统计
class SportStatic(models.Model):
    user = models.ForeignKey(User)
    points = models.IntegerField()
    steps = models.IntegerField()
    calories = models.FloatField(max_length=9)
    distance = models.FloatField(max_length=9)
    end_date = models.DateField()

# 运动目标
class SportConf(models.Model):
    user = models.ForeignKey(User)
    steps = models.IntegerField()
    calories = models.FloatField(max_length=9)
    create_time = models.DateTimeField()
    edit_time = models.DateTimeField()

# 运动明细
class SportDetail(models.Model):
    user = models.ForeignKey(User)
    create_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.IntegerField(null=True)
    type = models.CharField(max_length=20, null=True)
    points = models.IntegerField(null=True)
    steps = models.IntegerField(null=True)
    calories = models.FloatField(max_length=9, null=True)
    distance = models.FloatField(max_length=9)

#提醒设置
class Alarm(models.Model):
    type_id = models.IntegerField(choices=alarm_type_choices)
    critical = models.IntegerField()
    alarm_time = models.TimeField()
    alarm_channel = models.IntegerField(choices=alarm_channel_choices)

#商品
class Product(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=1000)
    price = models.FloatField()
    unit = models.CharField(max_length=10)
    discount = models.FloatField()
    is_delete = models.BooleanField(default=False)

#商品图片
class ProductPicture(models.Model):
    product = models.ForeignKey(Product)
    pic_path = models.FilePathField(path="/media/pro_img/")
    seq = models.IntegerField()
    is_delete = models.BooleanField(default=False)

#订单
class Order(models.Model):
    order_code = models.CharField(max_length=10)
    total_pay = models.FloatField(max_length=9)
    status = models.IntegerField(choices=order_status_choices)
    user = models.ForeignKey(User,db_column ="create_by")
    create_time = models.DateTimeField()

#订单明细
class OrderDetail(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    order_price = models.FloatField()
    product_price = models.FloatField()
    number = models.FloatField()
    total = models.FloatField()
