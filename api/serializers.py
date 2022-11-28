from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, ProductImage, Profile, Travel, Event, LocalCommunity, Booker, Booking, TravelComment, EventComment, LocalComment

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('pdu_name', 'pdu_img_name', 'pdu_img_url', 'pdu_ustr')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = '__all__'

class TravelCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelComment
        fields = '__all__'

class EventCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventComment
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalCommunity
        fields = '__all__'

class LocalCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalComment
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BookerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booker
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'