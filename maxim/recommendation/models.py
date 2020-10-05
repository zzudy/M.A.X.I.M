from django.db import models

# Create your models here.

class Academy(models.Model) : 
    Academy_id = models.IntegerField()
    location = models.CharField(max_length = 20)
    number = models.CharField(max_length = 20)
    name = models.CharField(max_length = 20)
    office_hour = models.IntegerField()
    
    def __str__(self):
        return self.name

class Class(models.Model) :
    class_id = models.IntegerField()
    name = models.CharField(max_length = 20)
    like = models.IntegerField()
    academy_name = models.CharField(max_length = 10, default='0000000')

    def __str__(self):
        return self.name

class Class_Description(models.Model) : 
    subject = models.CharField(max_length = 20)
    level = models.IntegerField()
    classSize = models.IntegerField(default= 0)
    teacherCareer = models.IntegerField()
    classHour = models.IntegerField()
    tuition = models.IntegerField()

    def __str__(self):
        return self.subject

class Profile(models.Model) :
    name = models.CharField(max_length = 20)
    profile_id = models.IntegerField()
    residence = models.CharField(max_length = 20)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Profile_preference(models.Model) : 
    classSize = models.IntegerField()
    teacherCareer = models.IntegerField()
    tuition = models.IntegerField()
    ageDistribition = models.IntegerField()

class Recommendation(models.Model):
    recommendation_id = models.IntegerField(default=0)
    classList = models.CharField(max_length = 20, default='0000000')

    def __str__(self):
        return self.classList

class RecommendationRequest(models.Model) :
    selected_class = models.CharField(max_length = 20)

class Request(models.Model) :
    request_id = models.IntegerField(default = 1)
    subjectName = models.CharField(max_length = 20)
    level = models.IntegerField(default= 0)
    day = models.IntegerField(default=0)
    time = models.IntegerField(default=0)