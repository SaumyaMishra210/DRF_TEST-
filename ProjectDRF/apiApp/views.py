from django.shortcuts import render ,get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status 
from .models import *
from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from django.contrib.auth.models import User 
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from datetime import datetime 
from . import helpers
from rest_framework.decorators import api_view , permission_classes
from rest_framework import viewsets
# Create your views here.    

# View set
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# function based view
@api_view()
@permission_classes([IsAuthenticated])
def getBook(request):
    items = Book.objects.filter(id= 1)
    serializer = BookSerializer(items, many=True)
    return Response({'status': "message from rest framework.", 'payload ': serializer.data})


class GeneratePdf(APIView):
    def get(self,request):
        userObj =   User.objects.all()
        params = {
            'today': datetime.today().date(),
            'userObj': userObj
        }
        file_name , status =helpers.save_pdf(params)
        
        return Response({"status":200,"path":f"media/{file_name}.pdf"})


# generic view

# ListAPIView : lists all the values from the DB.[GET]
# CreateAPIView : Create new object through an API.[POST]
# together perform Get and Post request inside single view.
@permission_classes([IsAdminUser])
class UserGeneric(generics.ListAPIView,generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer 

class UserGenericModify(generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer 
    lookup_filed = 'id'

class BookGeneric(generics.ListAPIView, generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 

# class based views
class UserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user,many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username = serializer.data['username'])
            
            token_obj = RefreshToken.for_user(user)
            access_token = token_obj.access_token

            response_data = {
                "status":status.HTTP_201_CREATED,
                'data': serializer.data,
                'refresh': str(token_obj),
                'access': str(token_obj.access_token)
                }
            return Response({"data":response_data,})
        return Response({"status":status.HTTP_400_BAD_REQUEST,"Error":serializer.errors})
    

class BookView(APIView):
    def get(self, request):
        items = Book.objects.all()
        serializer = BookSerializer(items, many=True)
        return Response({'status': "Data from Book Model.", 'payload ': serializer.data})

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.errors)
            response_data = {'message': 'data sent!','data': serializer.data}
            return Response(response_data, status=status.HTTP_201_CREATED )
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id, format=None):
        mymodel_instance = get_object_or_404(Book, pk=id)
        serializer = BookSerializer(mymodel_instance, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data updated successfully!', 'data': serializer.data}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id, format=None):
        # Fetch the object or return a 404 if not found
        my_object = get_object_or_404(Book, pk=id)
        
        # Deserialize and validate the partial update data
        serializer = BookSerializer(my_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request ):
        item_id = request.GET.get("id")
        mymodel_instance = Book.objects.get(id = item_id)
        # mymodel_instance = get_object_or_404(Item,pk= id)
        mymodel_instance.delete()
        return Response({'message': 'Data DELETED successfully!'},status=status.HTTP_204_NO_CONTENT)
 