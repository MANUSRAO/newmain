from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from .forms import StudentForm,MagStaffForm, ComplaintForm, ReviewForm
from .models import *
from django.db.models import Q
import pandas as pd
from datetime import date as dt,datetime,timedelta
from .serializers import studentSerializer,holidaySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from math import floor
from django.contrib.auth.decorators import login_required
from .decorators import not_allowed
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import View
from .utils import render_to_pdf 
from django.http import HttpResponse
# ----------------------------------------------------------------------------
'''
                        Common to Staff and Student 
'''
# -----------------------------------------------------------------------------

# 1. loginPage : Makes authentication of the user

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('Home')
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,"User Does Not Exist")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('Home')
        else:
            messages.error(request,"Username or Password does not exist")
    context = {}
    return render(request,'login_register.html',context)

# 2. logoutUser : logs the user out of the system

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')


# ----------------------------------------------------------------------------
'''
                            Hostel Staff Part
'''
# -----------------------------------------------------------------------------

# 1. base : This is function for home page, makes necessary queries for data visualization

@login_required(login_url='login')
def base(request):
    # If the user is Student then he is redirected to student accesible page only.
    if request.user.groups.exists():
        if request.user.groups.all()[0].name=="Student":
            return redirect('postComplaint')

    today = dt.today()
    reviews = Reviews.objects.all()
    today_reviews = reviews.filter(date=today).count()
    complaints = Complaints.objects.all()
    complaint_list = complaints[:5:-1]
    today_complaint = complaints.filter(date=today).count()
    week_complaint = complaints.filter(date__week=today.isocalendar()[1]).count()
    month_complaint = complaints.filter(date__month=today.month).count()
    start = today - timedelta(days=7)
    all_weekdays = [start + timedelta(days=d) for d in range(7) ]
    
    # Food Review Data Collection
    reviews_0 = reviews.filter(date=all_weekdays[0])
    morn_0=0
    aft_0=0
    night_0=0
    count_0 = 0
    for ele in reviews_0:
        morn_0 += ele.morn
        aft_0 += ele.aft
        night_0 += ele.night
        count_0+=1
    if count_0!=0:
        morn_0 = floor(morn_0/count_0)
        aft_0 = floor(aft_0/count_0)
        night_0 = floor(night_0/count_0)

    reviews_1 = reviews.filter(date=all_weekdays[1])
    morn_1=0
    aft_1=0
    night_1=0
    count_1 = 0
    for ele in reviews_1:
        morn_1 += ele.morn
        aft_1 += ele.aft
        night_1 += ele.night
        count_1+=1
    if count_1!=0:
        morn_1 = floor(morn_1/count_1)
        aft_1 = floor(aft_1/count_1)
        night_1 = floor(night_1/count_1)

    reviews_2 = reviews.filter(date=all_weekdays[2])
    morn_2=0
    aft_2=0
    night_2=0
    count_2 = 0
    for ele in reviews_2:
        morn_2 += ele.morn
        aft_2 += ele.aft
        night_2 += ele.night
        count_2+=1
    if count_2!=0:
        morn_2 = floor(morn_2/count_2)
        aft_2 = floor(aft_2/count_2)
        night_2 = floor(night_2/count_2)

    reviews_3 = reviews.filter(date=all_weekdays[3])
    morn_3=0
    aft_3=0
    night_3=0
    count_3 = 0
    for ele in reviews_3:
        morn_3 += ele.morn
        aft_3 += ele.aft
        night_3 += ele.night
        count_3+=1
    if count_3!=0:
        morn_3 = floor(morn_3/count_3)
        aft_3 = floor(aft_3/count_3)
        night_3 = floor(night_3/count_3)

    reviews_4 = reviews.filter(date=all_weekdays[4])
    morn_4=0
    aft_4=0
    night_4=0
    count_4 = 0
    for ele in reviews_4:
        morn_4 += ele.morn
        aft_4 += ele.aft
        night_4 += ele.night
        count_4+=1
    if count_4!=0:
        morn_4 = floor(morn_4/count_4)
        aft_4 = floor(aft_4/count_4)
        night_4 = floor(night_4/count_4)

    reviews_5 = reviews.filter(date=all_weekdays[5])
    morn_5=0
    aft_5=0
    night_5=0
    count_5 = 0
    for ele in reviews_5:
        morn_5 += ele.morn
        aft_5 += ele.aft
        night_5 += ele.night
        count_5+=1
    if count_5!=0:
        morn_5 = floor(morn_5/count_5)
        aft_5 = floor(aft_5/count_5)
        night_5 = floor(night_5/count_5)

    reviews_6 = reviews.filter(date=all_weekdays[6])
    morn_6=0
    aft_6=0
    night_6=0
    count_6 = 0
    for ele in reviews_6:
        morn_6 += ele.morn
        aft_6 += ele.aft
        night_6 += ele.night
        count_6+=1
    if count_6!=0:
        morn_6 = floor(morn_6/count_6)
        aft_6 = floor(aft_6/count_6)
        night_6 = floor(night_6/count_6)

    # Students Stats Collection
    all_student = Student.objects.all()
    first_students = all_student.filter(year="1")
    second_students = all_student.filter(year="2")
    third_students = all_student.filter(year="3")
    fourth_students = all_student.filter(year="4")
    pg_students = all_student.filter(year="PG")
    first_boys = first_students.filter(gender="M").count()
    first_girls = first_students.count() - first_boys
    second_boys = second_students.filter(gender="M").count()
    second_girls = second_students.count() - second_boys
    third_boys = third_students.filter(gender="M").count()
    third_girls = third_students.count() - third_boys
    fourth_boys = fourth_students.filter(gender="M").count()
    fourth_girls = fourth_students.count() - fourth_boys
    pg_boys = pg_students.filter(gender="M").count()
    pg_girls = pg_students.count() - pg_boys

    # Passing all collected data
    context = {
        'reviewCount':today_reviews,
        'first_students': first_students.count(),
        'second_students':second_students.count(),
        'third_students': third_students.count(),
        'fourth_students': fourth_students.count(),
        'pg_students': pg_students.count(),
        'first_boys': first_boys,
        'first_girls': first_girls,
        'second_boys': second_boys,
        'second_girls': second_girls,
        'third_boys': third_boys,
        'third_girls': third_girls,
        'fourth_boys': fourth_boys,
        'fourth_girls': fourth_girls,
        'pg_boys': pg_boys,
        'pg_girls': pg_girls,
        'studentCount': all_student.count(),
        'complaint_list':complaint_list,
        'dates_0':all_weekdays[0],
        'dates_1':all_weekdays[1],
        'dates_2':all_weekdays[2],
        'dates_3':all_weekdays[3],
        'dates_4':all_weekdays[4],
        'dates_5':all_weekdays[5],
        'dates_6':all_weekdays[6],
        'morn_0':morn_0,
        'aft_0':aft_0,
        'night_0':night_0,
        'morn_1':morn_1,
        'aft_1':aft_1,
        'night_1':night_1,
        'morn_2':morn_2,
        'aft_2':aft_2,
        'night_2':night_2,
        'morn_3':morn_3,
        'aft_3':aft_3,
        'night_3':night_3,
        'morn_4':morn_4,
        'aft_4':aft_4,
        'night_4':night_4,
        'morn_5':morn_5,
        'aft_5':aft_5,
        'night_5':night_5,
        'morn_6':morn_6,
        'aft_6':aft_6,
        'night_6':night_6,
        'today_complaint':today_complaint,
        'week_complaint':week_complaint,
        'month_complaint': month_complaint
    }
    return render(request,'index.html',context)


# 2. addStudent : Add student using staff access

@login_required(login_url='login')
@not_allowed(not_allowed=['Student'])
def addStudent(request):
    form = StudentForm()

    if request.method=='POST':
        form = StudentForm()
        form = form.save(commit=False)

        form.name = request.POST.get('name')
        form.room = request.POST.get('room')
        form.branch = request.POST.get('branch')
        form.year = request.POST.get('year')
        form.usn = request.POST.get('usn')
        form.pAdd = request.POST.get('pAdd')
        form.mobile = request.POST.get('mobile')
        form.email = request.POST.get('email')
        form.img = request.POST.get('img')
        form.blood = request.POST.get('blood')
        form.gender = request.POST.get('gender')
        form.save()

        username = form.email
        password = form.mobile+"@rvce"
        if User.objects.filter(username=username).exists():
            messages.error(request,"Student already exists.")  
        else:
            user = User.objects.create_user(username,username,password)
            user.save()
            studentGroup = Group.objects.get(name="Student")
            studentGroup.user_set.add(user)
            messages.success(request,"Student added successfully")
    context={}
    return render(request, 'addStudent.html', context)


# 3. upload : Upload Excel Sheet to add Student

@login_required(login_url='login')
@not_allowed(not_allowed=['Student'])
def upload(request):
    data = None
    if request.method == 'POST':
        new_file = request.FILES['myfile']

        data = pd.read_excel(new_file.read())

        for i in data.index:
            student = StudentForm()
            student = student.save(commit=False)
            student.name = data['name'][i]
            student.room = data['room'][i]
            student.branch = data['branch'][i]
            student.year = data['year'][i]
            student.usn = data['usn'][i]
            student.pAdd = data['pAdd'][i]
            student.mobile = data['mobile'][i]
            student.email = data['email'][i]
            student.img = data['img'][i]
            student.blood = data['blood'][i]
            student.save()
            username = student.email
            password = str(student.mobile)+"@rvce"
            if User.objects.filter(username=username).exists():
                messages.error(request,"One or more students already exists.")  
            else:
                user = User.objects.create_user(username,username,password)
                user.save()
                studentGroup = Group.objects.get(name="Student")
                studentGroup.user_set.add(user)
                messages.success(request,"Student added successfully")
    context = {'data':data}
    return render(request, 'upload.html', context)


# 4. createStaff : Add staff using staff access

@login_required(login_url='login')
@not_allowed(not_allowed=['Student'])
def createStaff(request):
    form = MagStaffForm()
    if request.method=='POST':
        form = MagStaffForm(request.POST)
        if form.is_valid():
            staff = MagStaffForm()
            staff = staff.save(commit=False)
            staff.name = form.cleaned_data['name']
            staff.mobile = form.cleaned_data['mobile']
            staff.email = form.cleaned_data['email']
            staff.designation = form.cleaned_data['designation']
            username = staff.email
            password = staff.mobile+"@rvce"
            if User.objects.filter(username=username).exists():
                messages.error(request,"Staff already exists")  
            else:
                user = User.objects.create_user(username,username,password)
                user.save()
                staff.save()
                messages.success(request,"Staff added successfully")     
        else:
            messages.error(request,"Error while creating Staff")  
    context = {'form':form}  
    return render(request,'staff_register.html',context)


# 5. readComplaint: Lists all complaints in recent order

@login_required(login_url='login')
@not_allowed(not_allowed=['Student'])
def readComplaint(request):
    complaints = Complaints.objects.all()

    context = {'complaints':complaints}
    return render(request, 'readComplaint.html', context)


#  6. indComplaint : Individual Complaint Page with date and description

@login_required(login_url='login')
@not_allowed(not_allowed=['Student'])
def indComplaint(request,pk):
    complaint = Complaints.objects.get(id=pk)
    context = {'complaint':complaint}
    return render(request,'indComplaint.html',context)


#  7. readReview : Lists all food reviews in recent order

@login_required(login_url='login')
@not_allowed(not_allowed=['Student'])
def readReview(request):
    reviews = Reviews.objects.all()
    context = {'reviews':reviews}
    return render(request, 'readReview.html', context)


#  8. findHoliday : Lists all holiday data, staff can search using start date and usn

@login_required(login_url='login')
@not_allowed(not_allowed=['Student'])
def findHoliday(request):
    holidays = None
    if request.method=='POST':
        q=request.POST.get('q')

        if(q==None):
            q=""
        else:
            q_date = q.split("-")
            if(len(q_date)>1):
                q_date = dt(int(q_date[2]),int(q_date[1]),int(q_date[0]))
            else:
                q_date = dt(2012,12,12)
        holidays = Holiday.objects.filter(
            Q(usn__icontains=q)|
            Q(startDate__date=q_date)
        )
        holidays = holidays[::-1]
    context = {'holidays':holidays}
    return render(request,'holiday_admin.html', context)


#  9. findStudent : Lists all student data, staff can search using usn, name and room. 
#  They can also visit student profiles, update and delete students.

@login_required(login_url='login')
@not_allowed(not_allowed=['Student'])
def findStudent(request):
    students = None
    if request.method=='POST':
        q=request.POST.get('q')
        if(q==None):
            q=""
        students = Student.objects.filter(
            Q(usn__icontains=q)|
            Q(name__icontains=q)|
            Q(room__icontains=q)
        )
    
    context = {'students':students}
    return render(request, 'findStudent.html', context)

#  10. studentProfile : View detailed student profile from Staff side

@login_required(login_url='login')
def studentProfile(request,pk):
    user = Student.objects.get(email=pk)
    context = {'user':user}
    return render(request, 'studentProfile.html', context)


#  11. updateStudent : Update student data

@login_required(login_url='login')
@not_allowed(not_allowed=['Student'])
def updateStudent(request, pk):
    student = Student.objects.get(usn=pk)
    form = StudentForm(instance=student)

    if request.method=='POST' :
        form = Student.objects.get(request.POST, instance=student)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'updateStudent.html', context)


#  12. deleteStudent : Delete Student data

@login_required(login_url='login')
@not_allowed(not_allowed=['Student'])
def deleteStudent(request, pk):
    student = Student.objects.get(usn=pk)
    user = User.objects.get(email=student.email)
    if request.method == 'POST':
        student.delete()
        user.delete()
        return redirect('Home')
    context = {'obj':student}
    return render(request, 'deleteStudent.html', context)


#  13. staffProfile : Individual Staff Profile

@login_required(login_url='login')
@not_allowed(not_allowed=['Student'])
def staffProfile(request):
    staff = MagStaff.objects.get(email=request.user.email)
    context = {'staff':staff}
    return render(request,'users-profile.html',context)

@login_required(login_url='login')
def sendMail(request):
    if request.method=='POST':
        message = request.POST['body']
        subject = request.POST['subject']
        email = request.POST['email']
        send_mail(
            subject,message,'settings.EMAIL_HOST_USER',[email],fail_silently=False
        )
        messages.success(request,"Email sent successfully")
    return render(request,'sendMail.html')
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
class MyPasswordChangeView(PasswordChangeView):
    template_name = 'changePassword.html'
    success_url = reverse_lazy('changePasswordDone')

class MyPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'passwordSuccess.html'


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        today = dt.today()
        reviews = Reviews.objects.all()
        today_reviews = reviews.filter(date=today).count()
        complaints = Complaints.objects.all()
        complaint_list = complaints[:5:-1]
        today_complaint = complaints.filter(date=today).count()
        week_complaint = complaints.filter(date__week=today.isocalendar()[1]).count()
        month_complaint = complaints.filter(date__month=today.month).count()
        start = today - timedelta(days=7)
        all_weekdays = [start + timedelta(days=d) for d in range(7) ]
        
        # Food Review Data Collection
        reviews_0 = reviews.filter(date=all_weekdays[0])
        morn_0=0
        aft_0=0
        night_0=0
        count_0 = 0
        for ele in reviews_0:
            morn_0 += ele.morn
            aft_0 += ele.aft
            night_0 += ele.night
            count_0+=1
        if count_0!=0:
            morn_0 = floor(morn_0/count_0)
            aft_0 = floor(aft_0/count_0)
            night_0 = floor(night_0/count_0)

        reviews_1 = reviews.filter(date=all_weekdays[1])
        morn_1=0
        aft_1=0
        night_1=0
        count_1 = 0
        for ele in reviews_1:
            morn_1 += ele.morn
            aft_1 += ele.aft
            night_1 += ele.night
            count_1+=1
        if count_1!=0:
            morn_1 = floor(morn_1/count_1)
            aft_1 = floor(aft_1/count_1)
            night_1 = floor(night_1/count_1)

        reviews_2 = reviews.filter(date=all_weekdays[2])
        morn_2=0
        aft_2=0
        night_2=0
        count_2 = 0
        for ele in reviews_2:
            morn_2 += ele.morn
            aft_2 += ele.aft
            night_2 += ele.night
            count_2+=1
        if count_2!=0:
            morn_2 = floor(morn_2/count_2)
            aft_2 = floor(aft_2/count_2)
            night_2 = floor(night_2/count_2)

        reviews_3 = reviews.filter(date=all_weekdays[3])
        morn_3=0
        aft_3=0
        night_3=0
        count_3 = 0
        for ele in reviews_3:
            morn_3 += ele.morn
            aft_3 += ele.aft
            night_3 += ele.night
            count_3+=1
        if count_3!=0:
            morn_3 = floor(morn_3/count_3)
            aft_3 = floor(aft_3/count_3)
            night_3 = floor(night_3/count_3)

        reviews_4 = reviews.filter(date=all_weekdays[4])
        morn_4=0
        aft_4=0
        night_4=0
        count_4 = 0
        for ele in reviews_4:
            morn_4 += ele.morn
            aft_4 += ele.aft
            night_4 += ele.night
            count_4+=1
        if count_4!=0:
            morn_4 = floor(morn_4/count_4)
            aft_4 = floor(aft_4/count_4)
            night_4 = floor(night_4/count_4)

        reviews_5 = reviews.filter(date=all_weekdays[5])
        morn_5=0
        aft_5=0
        night_5=0
        count_5 = 0
        for ele in reviews_5:
            morn_5 += ele.morn
            aft_5 += ele.aft
            night_5 += ele.night
            count_5+=1
        if count_5!=0:
            morn_5 = floor(morn_5/count_5)
            aft_5 = floor(aft_5/count_5)
            night_5 = floor(night_5/count_5)

        reviews_6 = reviews.filter(date=all_weekdays[6])
        morn_6=0
        aft_6=0
        night_6=0
        count_6 = 0
        for ele in reviews_6:
            morn_6 += ele.morn
            aft_6 += ele.aft
            night_6 += ele.night
            count_6+=1
        if count_6!=0:
            morn_6 = floor(morn_6/count_6)
            aft_6 = floor(aft_6/count_6)
            night_6 = floor(night_6/count_6)

        # Students Stats Collection
        all_student = Student.objects.all()
        first_students = all_student.filter(year="1")
        second_students = all_student.filter(year="2")
        third_students = all_student.filter(year="3")
        fourth_students = all_student.filter(year="4")
        pg_students = all_student.filter(year="PG")
        first_boys = first_students.filter(gender="M").count()
        first_girls = first_students.count() - first_boys
        second_boys = second_students.filter(gender="M").count()
        second_girls = second_students.count() - second_boys
        third_boys = third_students.filter(gender="M").count()
        third_girls = third_students.count() - third_boys
        fourth_boys = fourth_students.filter(gender="M").count()
        fourth_girls = fourth_students.count() - fourth_boys
        pg_boys = pg_students.filter(gender="M").count()
        pg_girls = pg_students.count() - pg_boys
        total_students = first_students.count() + second_students.count() + third_students.count() + fourth_students.count() + pg_students.count()
        total_boys = first_boys + second_boys + third_boys + fourth_boys + pg_boys
        total_girls = total_students - total_boys
        # Passing all collected data
        data = {
            'time':datetime.today(),
            'reviewCount':today_reviews,
            'first_students': first_students.count(),
            'second_students':second_students.count(),
            'third_students': third_students.count(),
            'fourth_students': fourth_students.count(),
            'pg_students': pg_students.count(),
            'first_boys': first_boys,
            'first_girls': first_girls,
            'second_boys': second_boys,
            'second_girls': second_girls,
            'third_boys': third_boys,
            'third_girls': third_girls,
            'fourth_boys': fourth_boys,
            'fourth_girls': fourth_girls,
            'pg_boys': pg_boys,
            'pg_girls': pg_girls,
            'studentCount': all_student.count(),
            'complaint_list':complaint_list,
            'dates_0':all_weekdays[0],
            'dates_1':all_weekdays[1],
            'dates_2':all_weekdays[2],
            'dates_3':all_weekdays[3],
            'dates_4':all_weekdays[4],
            'dates_5':all_weekdays[5],
            'dates_6':all_weekdays[6],
            'morn_0':morn_0,
            'aft_0':aft_0,
            'night_0':night_0,
            'morn_1':morn_1,
            'aft_1':aft_1,
            'night_1':night_1,
            'morn_2':morn_2,
            'aft_2':aft_2,
            'night_2':night_2,
            'morn_3':morn_3,
            'aft_3':aft_3,
            'night_3':night_3,
            'morn_4':morn_4,
            'aft_4':aft_4,
            'night_4':night_4,
            'morn_5':morn_5,
            'aft_5':aft_5,
            'night_5':night_5,
            'morn_6':morn_6,
            'aft_6':aft_6,
            'night_6':night_6,
            'today_complaint':today_complaint,
            'week_complaint':week_complaint,
            'month_complaint': month_complaint,
            'total_students':total_students,
            'total_boys':total_boys,
            'total_girls':total_girls
        }
        pdf = render_to_pdf('report.html',data)
        return HttpResponse(pdf, content_type='application/pdf')

# ----------------------------------------------------------------------------
'''
                            Student View Part
'''
# -----------------------------------------------------------------------------

# 1. postComplaint : To post complaint from the user side

@login_required(login_url='login')
def postComplaint(request):

    if request.method=='POST':
        complaint=request.POST.get('complaint')
        complaint_heading = request.POST.get('complaint_heading')
        form = ComplaintForm()
        form = form.save(commit=False)
        form.complaint=complaint
        form.complaint_heading = complaint_heading
        form.save()
        messages.success(request,"Complaint posted successfully")

    user = Student.objects.get(email=request.user.email)
    context = {'user':user}
    return render(request, 'postComplaint.html', context)


# 2. postReview : To post review from the user side

@login_required(login_url='login')
def postReview(request):

    if request.method=='POST':
        review=request.POST.get('review')
        morn = request.POST.get('morn')
        aft = request.POST.get('aft')
        night = request.POST.get('night')
        form = ReviewForm()
        form = form.save(commit=False)
        form.review=review
        form.morn = morn
        form.aft = aft
        form.night = night
        form.save()
        messages.success(request,"Review posted successfully")

    user = Student.objects.get(email=request.user.email)
    context = {'user':user}
    return render(request, 'postReview.html', context)


# 3. userProfile : To view Student profile from student side

@login_required(login_url='login')
def userProfile(request):
    user = Student.objects.get(email=request.user.email)
    context = {'user':user}
    return render(request, 'userProfile.html', context)


# ----------------------------------------------------------------------------
'''
                                API Part
'''
# -----------------------------------------------------------------------------

# 1. studentAPI : Used to "get" student card and "put" holiday status.

@api_view(['GET','PUT'])
def studentAPI(request,pk):
    try:
        student = Student.objects.get(usn=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer = studentSerializer(student)
        return Response(serializer.data)
    if request.method=='PUT':
        serializer = studentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# 2. holidayAPI : Used to "get" holiday data, "put" holiday updates, "post" holiday data.

@api_view(['GET','POST','PUT'])
def holidayAPI(request,pk):
    try:
        holiday = Holiday.objects.get(usn=pk,endDate=None)
    except Holiday.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer = holidaySerializer(holiday)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = holidaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    elif request.method=='PUT':
        serializer = holidaySerializer(holiday,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)