from django.db import models

# Create your models here.
class dairy_db(models.Model):
    user=models.CharField(max_length=40,unique=True)
    password=models.CharField(max_length=40)

    def __str__(self):
        return '%s,%s' % (self.user,self.password)

class contentdb(models.Model):
    user = models.ForeignKey(dairy_db,on_delete=models.CASCADE)
    date=models.CharField(max_length=20)
    content=models.CharField(max_length=10000)

    def __str__(self):
        return '%s,%s,%s' % (self.user,self.date,self.content)