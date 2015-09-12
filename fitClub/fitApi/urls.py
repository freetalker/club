from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from fitApi import views

urlpatterns = [
    # url(r'^api/user/$', views.user_list),
    # url(r'^api/user/(?P<pk>[0-9]+)/$', views.user_detail),
    url(r'^api/login/$',views.user_login),
    url(r'^api/user/profile/$',views.user_profile),
    url(r'^api/user/avatar/$',views.user_avatar),
    url(r'^api/sport/conf/$',views.sport_conf),
    url(r'^api/sport/stat/$',views.sport_stat),
    url(r'^api/sport/date/$',views.sport_date),
    url(r'^api/sport/rank/$',views.sport_rank),
    url(r'^api/sport/detail/$',views.sport_detail),
    url(r'^api/knowledge/list/$',views.knowledge_list),
    url(r'^api/knowledge/typeList/$',views.knowledge_type_list),
    url(r'^api/knowledge/newCount/$',views.knowledge_new_count),
    url(r'^api/knowledge/detail/$',views.knowledge_detail),
    url(r'^api/product/list/$',views.product_list),
    url(r'^api/product/detail/$',views.product_detail),
    url(r'^api/order/buy/$',views.order_buy),
    url(r'^api/order/list/$',views.order_list),
    url(r'^api/order/detail/$',views.order_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)