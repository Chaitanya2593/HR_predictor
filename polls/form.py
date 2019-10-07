from django.forms import ModelForm
from django import forms
from .models import dl_model

class FillForm(ModelForm):
    class Meta:
        model = dl_model
        exclude = ('Left', 'Dl model text')


class RawFillForm(forms.Form):

    DEPARTMENT_CHOICES = (
        ('sales','sales'),
        ('accounting', 'accounting'),
        ('hr', 'hr'),
        ( 'technical', 'technical'),
        ('support', 'support'),
        ('management', 'management'),
        ('IT', 'IT'),
        ('product_mng', 'product_mng'),
        ('marketing', 'marketing'),
        ('RandD', 'RandD'),
    )
    SALARY_CHOICES = (
        ('Low', 'Low'),
        ('High', 'High'),
        ('Medium', 'Medium'),
    )
    satisfaction_level = forms.DecimalField(label='satisfaction_level',
                                            widget=forms.TextInput(attrs={"placeholder":"0.00"}),
                                            required=True)
    last_evaluation = forms.DecimalField(label='last_evaluation',
                                            widget=forms.TextInput(attrs={"placeholder":"0.00"}))
    number_project = forms.IntegerField(label='number_project')
    average_montly_hours = forms.IntegerField(label='average_montly_hours')
    time_spend_company = forms.IntegerField(label='time_spend_company')
    Work_accident = forms.IntegerField(label='Work_accident')
    promotion_last_5years = forms.IntegerField(label='promotion_last_5years')
    department = forms.CharField(label='department', widget=forms.Select(choices=DEPARTMENT_CHOICES))
    salary = forms.CharField(label='salary', widget=forms.Select(choices=SALARY_CHOICES))

