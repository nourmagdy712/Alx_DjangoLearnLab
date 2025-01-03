from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model


User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    
   # For following, you can still provide a queryset because it's not read-only
    following = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    
    # For followers, since it's read-only, remove the queryset and just set read_only=True
    followers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()  # Using get_user_model() for flexibility
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True}  # Ensure password is not returned in responses
        }

    def create(self, validated_data):
        # Create the user object using get_user_model() instead of the direct User model
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        
        # Create the token for the user
        token = Token.objects.create(user=user)
        
        # Return the user along with the token
        return {
            'user': user,
            'token': token.key  # Return the token key (not the whole token object)
        }

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        # Validate the login credentials
        username = attrs.get('username')
        password = attrs.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError('Invalid username or password')

        if not user.check_password(password):
            raise serializers.ValidationError('Invalid username or password')

        # Create a token for the user (if the credentials are valid)
        token, created = Token.objects.get_or_create(user=user)
        
        return {
            'user': user,
            'token': token.key  # Return only the token key
        }
    
