from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission,IsAuthenticated

# Create your views here.
class Demo_view(APIView):
     permission_classes = [IsAuthenticated]
     def get(self,request):
         print(request.user)
         return Response({"sucess":"are you a IsAuthenticated"})
