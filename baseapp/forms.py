from django.forms import ModelForm
from .models import Student, MagStaff, Reviews, Complaints

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class MagStaffForm(ModelForm):
    class Meta:
        model = MagStaff
        fields = '__all__'

class ComplaintForm(ModelForm):
    class Meta:
        model = Complaints
        fields = '__all__'

class ReviewForm(ModelForm):
    class Meta:
        model = Reviews
        fields = '__all__'