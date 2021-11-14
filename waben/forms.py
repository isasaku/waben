from django import forms
from .models import Oder
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:  
        model = User
        fields = ("username","email",)    
    def save(self,commit=True):
        user = super().save(commit)
        user.save()
        return user

class OderForm(forms.ModelForm):
    class Meta:
        model = Oder
        fields = {
            'name',
            'month',
            'day1',
            'day2',
            'day3',
            'day4',
            'day5',
            'day6',
            'day7',
            'day8',
            'day9',
            'day10',
            'day11',
            'day12',
            'day13',
            'day14',
            'day15',
            'day16',
            'day17',
            'day18',
            'day19',
            'day20',
            'day21',
            'day22',
            'day23',
            'day24',
            'day25',
            'day26',
            'day27',
            'day28',
            'day29',
            'day30',
            'day31',
        }