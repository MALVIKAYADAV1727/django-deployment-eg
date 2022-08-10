from django.shortcuts import render
from django.http import HttpResponse
from appOne.models import Topic, Webpage, AccessRecord
from . import forms

# Create your views here.
# def index(request):
#     webpages_list = AccessRecord.objects.order_by('date')
#     date_dict= {'access_records' : webpages_list}
#     #my_dict={'insert_me' :'now i am coming from  appOne/index.html'}
#     return render(request, 'appOne/index.html', context=date_dict)

def index(request):
    return render(request, 'appOne/index.html')

def formNameView(request):
    form = forms.FormName()

    if request.method == 'POST':
        form= forms.FormName(request.POST)

        if form.is_valid():
            print('Validation success')
            print('Name: '+form.cleaned_data['name'])
            print('Email: '+form.cleaned_data['email'])
            print('Text: '+form.cleaned_data['text'])
    return render(request, 'appOne/form_page.html', {'form':form})
