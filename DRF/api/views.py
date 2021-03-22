from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.
#class based view
#@method_decorator(csrf_exempt, name='dispatch')
#class StudentAPI(View):
#    def get(self, request, *args, **kwargs)
#same content as method based views


#method based views
def student_detail(request): 
    stu = Student.objects.all()
    #stu = Student.objects.get(id = pk)
    #print(stu)
    serializer = StudentSerializer(stu, many = True)
    #print(serializer)
    json_data = JSONRenderer().render(serializer.data)
    #print(serializer.data)
    #print(json_data)
    #return HttpResponse(json_data, content_type = 'application/json')
    return JsonResponse(serializer.data, safe = False)


#create
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pydata = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pydata)
        if serializer.is_valid():
            serializer.save()
            response = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type = 'application/json')
        else:
            json_data = JSONRenderer.render(serializer.errors)
            return HttpResponse(json_data, content_type = 'application/json')

#read
@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu, many = False)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type = 'application/json')
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many = True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type = 'application/json')

#update 
@csrf_exempt
def student_update(request):
     if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pydata = JSONParser().parse(stream)
        id = pydata.get('id')
        stu = Student.objects.get(id= id)
        serializer = StudentSerializer(stu,data = pydata, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {'msg': 'Data Updates'}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type = 'application/json')
        else:
            json_data = JSONRenderer.render(serializer.errors)
            return HttpResponse(json_data, content_type = 'application/json')

#delete
@csrf_exempt
def student_delete(request):
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pydata = JSONParser().parse(stream)
        id = pydata.get('id')
        stu = Student.objects.get(id= id)
        stu.delete()
        response = {'msg':'Data deleted'}
        return JsonResponse(response, safe=False)
        # json_data = JSONRenderer().render(response)
        # return HttpResponse(json_data, content_type = 'application/json')