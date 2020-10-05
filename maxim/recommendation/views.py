from django.shortcuts import render, redirect
from .models import Class, Class_Description, Academy, Profile_preference, Request, Recommendation, RecommendationRequest
from .rcmd import getRecommendation, filtering
from .getcsv import saveinfo
from .forms import RequestForm, RecommendationRequestForm

def home(request) :
    # Information about class_description stored in DB 
    saveinfo()
    return render(request, 'home.html')

def request(request) :

    # pass form and save request to db
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            rq = form.save(commit=False)
            rq.save()
    else:
        form = RequestForm()
    return render(request, 'request.html', {'form' : form})

def recommendation(request) :

    rq = Request.objects.last()
    
    # Handing over the list of student preferences in order
    p = Profile_preference.objects.all()
    p_list = []
    p_list.insert(0, p[0].classSize)
    p_list.insert(1, p[0].tuition)
    p_list.insert(2, p[0].teacherCareer)
    p_list.insert(3, p[0].ageDistribition)

    # Return the recommended class id list by referring to filtered data and student preferences
    class_list = getRecommendation(filtering(rq.level), p_list)

    # Find class list with class id and save result to Recommendation
    for cid in class_list :
        c = Class.objects.filter(class_id = cid)
        r = Recommendation(recommendation_id = cid, classList = c[0].name)

        # Do not save duplicate values.
        dup = Recommendation.objects.filter(recommendation_id = cid)
        if(dup) : 
            continue
        else :
            r.save()

    # pass all recommendation objects under the name rcmd_class to the html file.
    rcmd_class = Recommendation.objects.all()
    
    # pass form and save request to db
    if request.method == "POST":
        form = RecommendationRequestForm(request.POST)
        if form.is_valid():
            rq = form.save(commit=False)
            rq.save()
    else:
        form = RecommendationRequestForm()

    return render(request, 'recommendation.html', {'rcmd_class' : rcmd_class, 'form': form})
    

def result(request) :
    rq = RecommendationRequest.objects.last()

    # Find class with class name
    my_class = Class.objects.filter(name = rq.selected_class)
    lk = my_class[0].like

    # Find class description with class name
    class_dscp = Class_Description.objects.filter(subject = rq.selected_class)

    # Find academy information with class name
    my_aca = Academy.objects.filter(name = my_class[0].academy_name)
    
    # Student can check his interest
    if request.method == "POST" : 
        my_class.update(like = lk+1)
        return redirect('result')
    else :
        return render(request, 'request.html',{'my_class' : my_class , 'class_dscp' : class_dscp , 'my_aca' : my_aca})
