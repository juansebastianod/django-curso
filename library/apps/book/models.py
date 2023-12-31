from django.db import models

# Create your models here.


class Author(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,blank=False,null=False)
    last_name=models.CharField(max_length=100,blank=False,null=False)
    nationality=models.CharField(max_length=50,blank=False,null=False)
    description=models.TextField(blank=False,null=False)
    
    
    class Meta:
        verbose_name:'Author'
        verbose_name_plural='Authors'
        ordering=['name']
        
    def __str__(self):
        return self.name
class Book(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100,blank=False,null=False)
    publication_date=models.DateField(blank=False,null=False)
    #author_id=models.OneToOneField(Author,on_delete=models.CASCADE)
    #author_id=models.ForeignKey(Author,on_delete=models.CASCADE)
    author_id=models.ManyToManyField(Author)
    class Meta:
        verbose_name:'Book'
        verbose_name_plural='Books'
        ordering=['title']
        
    def __str__(self):
        return self.title
    
    
    
    
    