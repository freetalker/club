from django.db import models

sex_choices = (
    (1, 'male'),
    (2, 'female'),
)

class User(models.Model):
    loginname = models.CharField(max_length=20, unique=True,null=False)
    password = models.CharField(max_length=20, null=False)
    nickname = models.CharField(max_length=20, null=True)
    realname = models.CharField(max_length=20)
    sex = models.IntegerField(choices=sex_choices)
    age = models.IntegerField(null=True)
    birthday = models.DateField()
    company = models.CharField(max_length=50, null=True)
    job = models.CharField(max_length=30,null=True)
    address = models.CharField(max_length=100,null=True)
    weixin = models.CharField(max_length=20,null=True)
    qq = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=30,null=True)
    identity = models.CharField(max_length=18,null=True)
    create_time = models.DateTimeField()
    create_by = models.IntegerField()
    is_active = models.BooleanField()
    last_login_time = models.DateTimeField(null=True)
    last_login_ip = models.CharField(max_length=40)

    def __unicode__(self):
        return self.loginname



