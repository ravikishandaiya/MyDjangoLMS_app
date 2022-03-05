# MyDjangoLMS_app
Backend and API end point for the following problem statement.

Problem Statement: Implement a library management system in which the user has to maintain information on books, authors, subscribers, book subscriptions and other components required in the library. He would need to design the tables as well as APIs for the same system and properly document the code as well. The APIs required would be - 
1. Add/View subscriber info, 
2. List all subscribers and their subscriptions, 
3. List all books, list available books, 
4. Place/View/Edit subscription which would be used to subscribe/return books, 
5. Add new books. 


Apart from this a periodic mail alert where the return date is in 2 days and a periodic mail alert which reminds the user every day after overdue should be implemented.

## API end points
## BOOKS
### Get All Books
Link: [localhost/books](localhost:8000/books)  <br />
Method: GET

### Add a book
Link: [localhost/books](localhost:8000/books)  <br />
Method: POST   <br />
Body 
```
{
  'book_id':'abc123',
  'name':'Book Name',
  'count': avilable books
}
```

### Get a specific book
Link: [localhost/books/<book_id>](localhost:8000/books/<id>)   <br />
Method: GET

### Update a specific book
Link: [localhost/books/<book_id>](localhost:8000/books/<id>)   <br />
Method: PUT  <br />
Body
```
{
  'book_id':'abc123',  // Id can't be changed if we have to first delete entry than make a new entry
  'name':'new Book Name',
  'count': updated avilable books
}
```

### Delete a book
Link: [localhost/books/<book_id>](localhost:8000/books/<id>)    <br />
Method: Delete





## SUBSCRIBERS
### Get All Subscribers
Link: [localhost/subscribers](localhost:8000/Subscribers)  <br />
Method: GET

### Add a Subscribers
Link: [localhost/subscribers](localhost:8000/Subscribers)  <br />
Method: POST   <br />
Body 
```
{
  'subscriber_id':'ABC123'
  'book_id':'abc123',
  'name':'Subscriber Name',
  'date': 'Today's date or book issue date, this feild is optional and automatically take today's date if date isn't provided' 
}
```

### Get a specific Subscribers with specific book
Link: [localhost/subscribers/"subscriber_id.book_id"](localhost:8000/subscribers/<id>)   <br />
Method: GET

### Update a specific Subscribers with specific book
Link: [localhost/subscribers/"subscriber_id.book_id"](localhost:8000/subscribers/<id>)   <br />
Method: PUT     <br />
Body
```
{
  'subscriber_id':'ABC123'
  'book_id':'abc123',
  'name':'Subscriber Name',
  'date': Optional
}
```

### Delete a Subscribers with specific book
Link: [localhost/subscribers/"subscriber_id.book_id"](localhost:8000/subscribers/<id>)    <br />
Method: Delete



 <br />
  <br />

**Thanks to all of you For showing intrest**  <br />
**Happy to Hear from you, any suggetions...**


