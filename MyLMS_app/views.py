from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Books,Subscribers
from . serializers import BooksSerializer, SubscribersSerializer, DistinctSubscribers
from rest_framework.decorators import api_view

# Create your views here.
## Manually from HERE

def index(request):
    return HttpResponse("Welcome to a very simple and intrective Library Management System.")


@api_view(['GET', 'POST'])
def books(request):
    if request.method == 'GET':
        books = Books.objects.all()
        serializer = BooksSerializer(books, many=True)
        return Response(serializer.data)      

    elif request.method == 'POST':
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)


@api_view(['GET', 'PUT','DELETE'])
def books_by_id(request, id):
    try:
        book = Books.objects.get(book_id=str(id))
    except Books.DoesNotExist:
        return Response({'message': 'The Book does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        book = Books.objects.get(book_id=id)
        serializer = BooksSerializer(book, many=False)
        return Response(serializer.data) 
    
    elif request.method == 'PUT': 
        book = Books.objects.get(book_id=id)
        try:
            book.name = request.data['name']
        except:
            pass
        try:
            book.count = request.data['count']
        except:
            pass
        book.save()        
        serializer = BooksSerializer(book, many=False)
        return Response(serializer.data)

    elif request.method == 'DELETE': 
        book = Books.objects.get(book_id=id)
        book.delete() 
        return Response({'message': 'Book was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    
@api_view(['GET','POST'])
def subscribers(request):
    if request.method == 'GET':
        subscriber = Subscribers.objects.all()
        serializer = SubscribersSerializer(subscriber, many=True)
        return Response(serializer.data)      

    elif request.method == 'POST':
        serializer = SubscribersSerializer(data=request.data)
        if serializer.is_valid():
            try:
                print(request.data)
                a = request.data
                book = Books.objects.get(book_id=a['book_id'])
            except Books.DoesNotExist:
                return Response({'message': 'The Book does not exist'}, status=status.HTTP_404_NOT_FOUND)

            book = Books.objects.get(book_id=request.data['book_id'])
            if book.count > 0:
                serializer.save()
                book.count-=1
                book.save()
                return Response(serializer.data)
            else:
                return Response({'message': 'Currently Book Not avilable, all books are issued!'}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.data)


@api_view(['GET', 'PUT','DELETE'])
def subscribers_by_id(request, ids):
    a = ids.split(".")
    sub_id = a[0]
    book_id = a[1]
    try:
        subscriber = Subscribers.objects.get(subscriber_id=sub_id, book_id=book_id)
    except Subscribers.DoesNotExist:
        return Response({'message': 'The Subscribers with the given book id does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        subscriber = Subscribers.objects.get(subscriber_id=sub_id, book_id=book_id)
        serializer = SubscribersSerializer(subscriber, many=False)
        return Response(serializer.data) 
    
    elif request.method == 'PUT': 
        subscriber = Subscribers.objects.get(subscriber_id=sub_id, book_id=book_id)
        try:
            subscriber.name = request.data['name']
        except:
            pass
        try:
            subscriber.date = request.data['date']
        except:
            pass
        subscriber.save()
        serializer = SubscribersSerializer(subscriber, many=False)
        return Response(serializer.data)

    elif request.method == 'DELETE': 
        subscriber = Subscribers.objects.get(subscriber_id=sub_id, book_id=book_id)
        subscriber.delete() 
        book = Books.objects.get(book_id=book_id)
        book.count+=1
        book.save()
        return Response({'message': 'Subscriber with given book id was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def distinct_subscribers(request):
    if request.method == 'GET':
        subscriber = Subscribers.objects.values('subscriber_id', 'name').distinct().order_by('name')
        serializer = DistinctSubscribers(subscriber, many=True)
        return Response(serializer.data) 
    else:
        return Response({'message': 'Wrong Method ! Allowed Method: GET.'})
