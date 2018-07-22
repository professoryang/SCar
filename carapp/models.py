from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50, verbose_name='用户名')
    passwd = models.CharField(max_length=50, verbose_name='口令')
    email = models.CharField(max_length=50, verbose_name='邮箱')
    phone = models.CharField(max_length=12, verbose_name='电话')
    img = models.ImageField(verbose_name='头像', upload_to='user/images')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 's_user'
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name


class Brand(models.Model):
    url = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 's_brand'


class Outer(models.Model):
    name = models.CharField(max_length=200)
    kind = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 's_outer'


class Letter(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 's_letter'


class Pinpai(models.Model):
    name = models.CharField(max_length=100)
    letter = models.ForeignKey(Letter, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 's_pinpai'


class Chexi(models.Model):
    name = models.CharField(max_length=100)
    pinpai = models.ForeignKey(Pinpai, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 's_chexi'

