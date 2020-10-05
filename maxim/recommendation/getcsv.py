import csv
import os

from .models import Class_Description

def saveinfo() :
    path = "/Users/surin/Documents/201720723/3-1/도메인분석및SW설계/Final/rcmd/"
    os.chdir(path)
    with open('finalAcademy.csv') as csvfile :
        reader = csv.DictReader(csvfile)
        for row in reader :
            c = Class_Description(subject = row['class_name'], level = row['level'], teacherCareer = row['careerOfTeacher'], classHour = row['class_hour_time'][0], tuition = row['tuition'], classSize = row['class_size'])
            
            # class name이 겹치면 저장 X
            dup = Class_Description.objects.filter(subject = row['class_name'])
            
            if(dup) : 
                continue
            else :
                c.save()