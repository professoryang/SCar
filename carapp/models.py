from django.db import models


# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=50, verbose_name='用户名')
    passwd = models.CharField(max_length=50, verbose_name='口令')
    passwd2 = models.CharField(max_length=50, verbose_name='确认口令')
    email = models.CharField(max_length=50, verbose_name='邮箱')
    phone = models.CharField(max_length=12, verbose_name='电话')
    img = models.ImageField(verbose_name='头像',
                            upload_to='user/images',
                            )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 's_user'
        verbose_name = '二手车管理'
        verbose_name_plural = verbose_name
