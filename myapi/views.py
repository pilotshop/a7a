from django.shortcuts import render
from django.http.response import JsonResponse,HttpResponse
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import locationSerializer
from rest_framework import status,filters
# Create your views here.
def no_rest_no_model(request):
    guest =[
        {'name':'sai','email':'sai@123','phone':123456789},
        {'name':'sai1','email':'sai1@123','phone':123456789},
        {'name':'sai2','email':'sai2@123','phone':23456789},
    ]
    return JsonResponse(guest, safe=False)
def no_rest_model(request):
    data = location.objects.all()
    return JsonResponse(list(data.values()), safe=False)

@api_view(['GET','POST'])

def graduationproject(request):
    if request.method == 'GET':
        data = location.objects.all()
        serializer = locationSerializer(data,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = locationSerializer(data=request.data)
    if serializer.is_valid():   
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    # guest.objects.create(name=data['name'],emaiyl=data['email'],phone=data['phone'])
    return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def graduationproject2(request,pk):
    try:
        data = location.objects.get(pk=pk)
    except location.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = location.objects.get(pk=pk)
        serializer = locationSerializer(data)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = locationSerializer(data,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)