from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=32, verbose_name="姓名")
    admission = models.CharField(max_length=32, verbose_name="准考证编码")
    type = models.CharField(max_length=32, verbose_name="类型", default="C1")
    code = models.CharField(max_length=18, verbose_name="身份证")
    one = models.CharField(max_length=10, verbose_name="科目一", default="**")
    two = models.CharField(max_length=10, verbose_name="科目二", default="**")
    three = models.CharField(max_length=10, verbose_name="科目三", default="**")
    four = models.CharField(max_length=10, verbose_name="科目四", default="**")

