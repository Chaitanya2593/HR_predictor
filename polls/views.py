from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from polls.models import dl_model
from .form import FillForm, RawFillForm
import urllib.request
import json


def index(request):
    latest_dl_models = dl_model.objects.all()
    context = {"latest_dl_models": latest_dl_models}
    return render(request, 'polls/index.html', context)

# def form(request):  # working
#     form = FillForm(request.POST or None)
#     if form.is_valid():
#         field_item = form.save(commit=False)
#         field_item.save()
#         form = FillForm()
#     else:
#         form = FillForm()
#     context = {'form': form}
#     return render(request, 'polls/form.html', context)

def form(request):
    form = RawFillForm(request.POST or None)
    result=""
    if form.is_valid():
        # field_item = form.save(commit=False)
        # field_item.save()
        print(form.cleaned_data)
        result = define_model(form.cleaned_data)
        print(result)
#         form = RawFillForm()
    else:
        form = RawFillForm()

    context = {'form': form, 'result': result}
    return render(request, 'polls/form.html', context)

def define_model(paramters):
    print(paramters)
    data = {
        "Inputs": {
            "input1":
    [
#         paramters
            {
                'satisfaction_level': str(remov_decimal(paramters['satisfaction_level'])), 
                'last_evaluation': str(remov_decimal(paramters['last_evaluation'])), 
                'number_project':  str(paramters['number_project']), 
                'average_montly_hours':  str(paramters['average_montly_hours']), 
                'time_spend_company':  str(paramters['time_spend_company']), 
                'Work_accident':  str(paramters['Work_accident']), 
                'promotion_last_5years':  str(paramters['promotion_last_5years']), 
                'department':  str(paramters['department']), 
                'salary':  str(paramters['salary']), 
                'left': '',
                }
        ],
             



#             "input1":
#                  [
#                     {
#                             'satisfaction_level': "0.38",   
#                             'last_evaluation': "0.74",   
#                             'number_project': "4",   
#                             'average_montly_hours': "215",   
#                             'time_spend_company': "3",   
#                             'Work_accident': "0",   
#                             'left':"",
#                             'promotion_last_5years': "0",   
#                             'department': "sales",   
#                             'salary': "Low"   ,
#                     }
#                 ],
        },
        "GlobalParameters":  {
        }
    }
    body = str.encode(json.dumps(data))
    url = {AZureMlURL}
    api_key = {AZureMlAPI_Key}
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    req = urllib.request.Request(url, body, headers)
    try:
        response = urllib.request.urlopen(req)
        result = response.read()        
        result = json.loads(result,encoding='utf-8')
        print(result['Results']['output1'][0])        
        return result['Results']['output1'][0]['Scored Labels']
    
    except urllib.error.HTTPError as error:
        # print("The request failed with status code: " + str(error.code))
        # # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        # print(error.info())
        # print(json.loads(error.read().decode("utf8", 'ignore')))
        # return " The request failed with status code: " + str(error.code)
        return " The request failed with status code: " + str(error.code)

def remov_decimal(attribute):
    attribute= str(attribute).replace("Decimal", '')
    attribute= attribute.replace("(", '')
    return attribute.replace(")", '')
