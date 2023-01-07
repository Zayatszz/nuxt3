from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from .models import Category, News


class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=get_user_model().objects.all())]
    )
    
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    
    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8},
            'first_name': {'required': True},
            'last_name': {'required': True}
        }
    
    def create(self, validated_data):
        user = self.Meta.model.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
    
class UserSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)
    
    class Meta:
        model = get_user_model()
        fields = ('id','email', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8},
        }


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ("id", "name", "description", "icon", "order")
        
class NewsSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    user_name = serializers.CharField(source='user.first_name')

    class Meta:
        model=News
        fields = ("__all__")

  # fields = ("id", "user", "title", "picture", "content", "creation_date", "publish_date", "view", "category", "category_name")
        
        
