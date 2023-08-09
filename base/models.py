from django.db import models

# Create your models here.

class ProjectCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    
class Portfolio(models.Model):
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    body = models.TextField()
    photo = models.FileField(upload_to='images/')
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Loyihalar"

    def __str__(self):
        return self.title
    
class Member(models.Model):
    full_name = models.CharField(max_length=30)
    occupation = models.CharField(max_length=25)
    photo = models.FileField(upload_to='images/')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Bizning jamoa a'zolari"

    def __str__(self):
        return self.full_name
    
class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Kategoriya"

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=250)
    body = models.TextField()
    photo = models.FileField(upload_to='images/')
    date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Blog"

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    message = models.TextField()

    class Meta:
        verbose_name_plural = "Xabarlar"

    def __str__(self):
        return self.full_name
