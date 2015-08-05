from django.conf.urls import url
from fitAdmin import views

urlpatterns = [
    url(r'^admin/$', views.admin),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'fitClub/login.html'}),
    url(r'^admin/user/list$',views.user_list),
    url(r'^admin/product/list$',views.product_list),
    url(r'^admin/order/list$',views.orders_list),
    url(r'^admin/stat/user$',views.stat_user),
    url(r'^admin/stat/sport$',views.stat_sport),
    url(r'^admin/config/base/$',views.conf_base),
    url(r'^admin/config/alarm/$',views.conf_alarm),
    url(r'^admin/file/upload/$',views.upload_file),
]
