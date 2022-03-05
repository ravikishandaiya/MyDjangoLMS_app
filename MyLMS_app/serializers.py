from rest_framework import serializers
from . models import Books,Subscribers

class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = '__all__'

class SubscribersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subscribers
        fields = '__all__'

class DistinctSubscribers(serializers.ModelSerializer):

    class Meta:
        model = Subscribers
        fields = ('subscriber_id', 'name')
