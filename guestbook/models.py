from django.db import models

# Create your models here.
class GuestBook(models.Model):
    id = models.AutoField(primary_key=True)
    writer = models.CharField(verbose_name='작성자', max_length=30)
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='생성 일시', auto_now_add=True)
    