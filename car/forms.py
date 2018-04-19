# -*- encoding: utf-8 -*-
from django import forms
from car.models import *

class CreateCarForm(forms.ModelForm):
    title = forms.CharField(
        label="Name(Team, Phone)",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'readonly': 'readonly'
            }
        )
    )

    start_time = forms.CharField(
        label="Start Time",
        widget=forms.DateTimeInput(
            attrs={
                'class': 'form-control',
                'readonly': 'readonly'
            }
        )
    )

    end_time = forms.CharField(
        label="End Time",
        widget=forms.DateTimeInput(
            attrs={
                'class': 'form-control',
                'readonly': 'readonly'
            }
        )
    )

    car_id = forms.CharField(
        label="Car",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'readonly': 'readonly'
            }
        )
    )

    passenger = forms.CharField(
        label="Passengers",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',      
                'placeholder': '탑승자 전체 기입',
                'required': 'true',          
            }
        )
    )

    purpose = forms.CharField(
        label="Purpose",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',      
                'placeholder': '예) IoT서비스 실차 실험',
                'required': 'true',          
            }
        )
    )

    destination = forms.CharField(
        label="Destination",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',      
                'placeholder': '예) 춘천 남이섬',
                'required': 'true',          
            }
        )
    )

    checkflag = forms.BooleanField(        
        widget=forms.CheckboxInput(
            attrs={
                'required': 'true',          
            }
        )
    )    

    class Meta:
        model = BookingCarInfo
        fields = ("title", "start_time", "end_time", "car_id", "passenger", "purpose", "destination",)
