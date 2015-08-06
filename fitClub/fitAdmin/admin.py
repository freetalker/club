from django.contrib import admin

from fitAdmin.models import *

admin.site.register(User)
admin.site.register(MemberLevel)
admin.site.register(Member)

admin.site.register(Device)
admin.site.register(DeviceBrand)
admin.site.register(DeviceUser)

admin.site.register(HealthBloodPress)
admin.site.register(HealthSleep)
admin.site.register(HealthWeight)

admin.site.register(Alarm)

admin.site.register(Product)
admin.site.register(ProductPicture)

admin.site.register(Order)
admin.site.register(OrderDetail)

admin.site.register(SportDate)
admin.site.register(SportConf)
admin.site.register(SportDetail)
admin.site.register(SportStat)