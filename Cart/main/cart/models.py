from django.db import models
class sell(models.Model):
    snum=models.CharField(max_length=30)
    mail=models.EmailField()
    pno=models.IntegerField()
    pnum=models.CharField(max_length=50)
    pr=models.IntegerField()
    cnt=models.IntegerField(default=10)
    pd=models.TextField()
    _pvt=models.CharField(max_length=11,default=0)
    img=models.ImageField(upload_to='media/products/img')
    def __str__(self):
        return self.snum
class buy(models.Model):
    bnam=models.CharField(max_length=30)
    gm=models.EmailField()
    ph=models.IntegerField()
    dob=models.DateTimeField(default=None, blank=True, null=True)
    _bpt=models.CharField(max_length=11)
    avl=models.BooleanField(default=False)
    def __str__(self):
        return self.bnam