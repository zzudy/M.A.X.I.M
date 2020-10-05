from django.contrib import admin

from .models import Class, Profile, Profile_preference, Recommendation, Request, Class_Description, Academy, RecommendationRequest

# Register your models here.
admin.site.register(Academy)
admin.site.register(Class)
admin.site.register(Class_Description)
admin.site.register(Profile)
admin.site.register(Profile_preference)
admin.site.register(Recommendation)
admin.site.register(RecommendationRequest)
admin.site.register(Request)