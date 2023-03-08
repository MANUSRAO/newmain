from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    room = models.CharField(max_length=10,blank=True)
    branch = models.CharField(max_length=10)
    year = models.CharField(max_length=10)
    usn = models.CharField(max_length=12,blank=True,primary_key=True)
    pAdd = models.CharField(max_length=250)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    img = models.CharField(max_length=200,blank=True)
    blood = models.CharField(max_length=10)
    onHoliday = models.BooleanField(default=False)
    gender = models.CharField(max_length=1,blank=False)
    def __str__(self):
        return self.name+" "+self.usn

class MagStaff(models.Model):
    email = models.EmailField(max_length=254, primary_key=True)
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=30)
    mobile = models.CharField(max_length=10, blank=True)
    def __str__(self):
        return self.name
    
class Holiday(models.Model):
    usn = models.CharField(max_length=12)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField(null=True,blank=True)
    numberOfDays = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.usn

class Complaints(models.Model):
    complaint_heading = models.CharField(max_length=50)
    complaint = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.complaint_heading)

    class Meta:
        ordering = [ '-date' ]

class Reviews(models.Model):
    review = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)
    morn = models.IntegerField(default=5)
    aft = models.IntegerField(default=5)
    night = models.IntegerField(default=5)

    def __str__(self):
        return self.review

    class Meta:
        ordering = [ '-id' ] 