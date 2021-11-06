from django.db import models

# Create your models here.

class Cast(models.Model):
    name = models.CharField(max_length=255)

    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Cast'


class Category(models.Model):
    category = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.category
    class Meta:
        verbose_name = 'Category'  

class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(verbose_name='Movie Description')
    language = models.CharField(max_length=25)
    running_time = models.IntegerField()
    image = models.ImageField(upload_to='photo/%y/%m/%d', null=True, blank=True)
    active = models.BooleanField(default=False)
    rate = models.IntegerField()
    release_date = models.DateField(null=True,blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    #relation
    # category = models.ForeignKey(Category,on_delete=models.PROTECT, default='drama')
    # cast = models.ManyToManyField('movie.Cast_Mem', through='Cast')
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'movie'
        ordering = ['id']    



               