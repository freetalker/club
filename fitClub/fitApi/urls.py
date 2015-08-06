from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from fitApi import views

urlpatterns = [
    url(r'^api/user/$', views.user_list),
    url(r'^api/user/(?P<pk>[0-9]+)/$', views.user_detail),
    url(r'^api/login/$',views.user_login),
    url(r'^api/user/profile/$',views.user_profile),
    url(r'^api/user/avatar/$',views.user_avatar),
    url(r'^api/sport/conf/$',views.sport_conf),
]

urlpatterns = format_suffix_patterns(urlpatterns)