## APIs

### GET 

1. Returns list of all posts made

```localhost:8000``` 

2. Returns post with id

```localhost:8000/<id>```

### POST
1. Create new post. 

```localhost:8000``` 

With body (in json format):

```
{
    "title": "TITLE GOES HERE",
    "message": "MESSAGE GOES HERE"
}
```

### PUT

1. Update a Post with id. 

```localhost:8000/<id>``` 

Updated content in body (in JSON format):

```
{
    "title": "NEW TITLE GOES HERE",
    "message": "NEW MESSAGE GOES HERE"
}
```

### DELETE

1. Delete Post with id

```localhost:8000/<id>```
 
 ## Running the project
 
 Start with
 
 ```docker-compose up```