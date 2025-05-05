from django.db import models

class Book(models.Model): 
    title = models.CharField(max_length = 50) 
    author = models.CharField(max_length = 50) 
    price = models.FloatField(default = 0.0) 
    edition = models.SmallIntegerField(default = 1)
    
class Address(models.Model):
    city = models.CharField(max_length=30)
    
class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    
class Card(models.Model):
    card_number = models.IntegerField()
    
class Department(models.Model):
    name = models.CharField(max_length=50)
    
class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.IntegerField()
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    card = models.ForeignKey(Card, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    courses = models.ManyToManyField(Course)
    
    
class Address2(models.Model):
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street}, {self.city}"
    
class Students2(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    addresses = models.ManyToManyField(Address2)

    def __str__(self):
        return self.name
    
class GalleryImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    