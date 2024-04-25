from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=50, null= True)
    slug = models.SlugField(max_length=50 , unique= True , null= True)



      
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=50, null= True)
    slug = models.SlugField(max_length=50 , unique= True , null= True)



      
    def __str__(self):
        return self.name

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, null= True , blank= True, on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tag , blank=True, )
    description = models.TextField(max_length=200, blank = True)
    image = models.ImageField(upload_to ='trainer/%Y/%m/%d/', null = True)


    
    def __str__(self):
        return self.name
