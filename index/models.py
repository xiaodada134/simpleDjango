from django.db import models

# Create your models here.
class Users(models.Model):
        id = models.IntegerField(
            primary_key=True
        )
        uname = models.CharField(
            max_length=20,
            unique=1,
            verbose_name='姓名'
        )
        upwd = models.CharField(
            max_length=50,
            verbose_name='密码'
        )
        is_active = models.BooleanField(default=1, verbose_name='是否激活')

        def __str__(self):
            return self.uname

        class Meta:
            db_table = 'users'
            verbose_name = '用户'
            verbose_name_plural = verbose_name

# # 记录最近一次的登录时间
# class Last_login(models.Model):
#         id = models.IntegerField(
#             primary_key=True
#         )
#         login_username = models.OneToOneField(Users, verbose_name='登录用户')
#         login_time = models.DateTimeField(auto_now_add=True)
#
#         def __str__(self):
#             return self.name
#
#         class Meta:
#             db_table = 'login_time'
#             verbose_name = '登录时间'
#             verbose_name_plural = verbose_name


