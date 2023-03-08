from django.urls import path
from . import views
from .views import GeneratePdf
urlpatterns = [
       path('', views.base, name="Home"),
       path('login/',views.loginPage,name="login"),
       path('logout/',views.logoutUser,name="logout"),
       path('register/',views.addStudent,name="register"),
       path('staff_register/',views.createStaff,name="staff_register"),
       path('studentAPI/<str:pk>/',views.studentAPI,name="studentAPI"),
       path('holiday/<str:pk>/',views.holidayAPI,name="holidayAPI"),
       path('readComplaint/',views.readComplaint,name="readComplaint"),

       path('postComplaint/',views.postComplaint,name="postComplaint"),
       path('postReview/',views.postReview,name="postReview"),
       path('password/<str:pk>/', views.MyPasswordChangeView.as_view(), name='changePassword'),
       path('password/done', views.MyPasswordChangeDoneView.as_view(), name="changePasswordDone"),
       path('readReview/',views.readReview,name="readReview"),
       path('userProfile/',views.userProfile,name="userProfile"),
       path('studentProfile/<str:pk>/',views.studentProfile,name="studentProfile"),
       path('addStudent/', views.addStudent, name="addStudent"),
       path('findStudent/', views.findStudent, name="findStudent"),
       path('updateStudent/<str:pk>/', views.updateStudent, name="updateStudent"),
       path('deleteStudent/<str:pk>/', views.deleteStudent, name="deleteStudent"),
       path('upload', views.upload, name="upload"),
       path('holidaylist',views.findHoliday,name="holidayList"),
       path('staffProfile/',views.staffProfile,name="staffProfile"),
       path('complaint/<int:pk>',views.indComplaint,name="indComplaint"),
       path('sendMail/',views.sendMail,name="sendMail"),
       path('pdf/', GeneratePdf.as_view(),name='pdf')
]