from rest_framework import serializers
from .models import  *
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['cat_name']

class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = '__all__'
    
    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category, created = Category.objects.get_or_create(**category_data)
        book = Book.objects.create(category=category, **validated_data)
        return book

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password']

    def create(self, validated_data):
        # Extract password and create user with password hashing
        user = User.objects.create_user(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user