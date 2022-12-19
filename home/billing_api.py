from .billingSr import*
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import students

class employeeAPI(APIView):
    def get(self,request):
        anuj=students.objects.all()
        serializer=customerserializer(anuj,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = customerserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "User created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        box = students.objects.get(pk=id)
        serializer = customerserializer(box, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "User Detail Updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        id = pk
        boxs = students.objects.get(pk=id)
        boxs.delete()
        return Response({"Message": "User Deleted"})