from django.shortcuts import render
from .models import *
from .serializers import StudentSerializer
from django.http import HttpResponse,JsonResponse
from rest_framework.renderers import JSONRenderer

# queryset for all student data in json format/response
# json python built-in package which is used to work with json data
# dumps(data)-> convert into python object into json string
# loads(data)-> convert jsonstring into python object
# def Studentdetail(request):
#     studentdata = Student.objects.all()
#     serializer = StudentSerializer(studentdata,many=True)
#     json_data = JSONRenderer().render(serializer.data)
#     # return JsonResponse(serializer.data)
#     return HttpResponse(json_data,content_type='application/json')

def Studentdetail(request,id):
    studentdata = Student.objects.get(id=id)
    serializer = StudentSerializer(studentdata)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')