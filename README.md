# To launch web service:

```git clone cd Web_Services```

```docker-compose up```

Use postman to test HTTP methods: https://www.postman.com/downloads/

# Internet Store

GET

### READ 

Get all items: 

```curl -X GET http://localhost:5000/items``` 

Get all users: 

```curl -X GET http://localhost:5000/users```

Get all shops: 

```curl -X GET http://localhost:5000/shops``` 

Get specific item: 

```curl -X GET http://localhost:5000/items/2``` 

Get specific user: 

```curl -X GET http://localhost:5000/users/1``` 

Get specific shop: 

```curl -X GET http://localhost:5000/shops/1```

POST 

### CREATE 

Create an item:

```curl -X POST http://localhost:5000/items -H "Content-Type: application/json" -d '{"title": "New Item", "manufacturer": "New Manufacturer"}' ```

Create a user: 

```curl -X POST http://localhost:5000/users -H "Content-Type: application/json" -d '{"name": "John Smith"}' ```

Create a shop: 

```curl -X POST http://localhost:5000/shops -H "Content-Type: application/json" -d '{"address": "123 Main St"}'```

PUT 

### UPDATE 

Upadate an item: 

```curl -X PUT http://localhost:5000/items/1 -H "Content-Type: application/json" -d '{"title": "Updated Item", "manufacturer": "Updated Manufacturer"}' ```

Update a user: 

```curl -X PUT http://localhost:5000/users/1 -H "Content-Type: application/json" -d '{"name": "Updated Name"}'``` 

Update a shop: 

```curl -X PUT http://localhost:5000/shops/1 -H "Content-Type: application/json" -d '{"address": "Updated Address"}' ```

Assign user to an item: 

```curl -X PUT http://localhost:5000/items/1/user/1 ```

Assign item to a shop: 

```curl -X PUT http://localhost:5000/items/1/shop/1```

### DELETE 

DELETE 

Delete an item: 

```curl -X DELETE http://localhost:5000/items/1 ```

Delete a user: 

```curl -X DELETE http://localhost:5000/users/2 ```

Delete a shop: 

```curl -X DELETE http://localhost:5000/shops/1``` 

Unasign user from an item: 

```curl -X DELETE http://localhost:5000/items/1/user```

Unasign item from a shop:

```curl -X DELETE http://localhost:5000/items/1/shop```

# Plant Shop

### CREATE:
Create plant:
```curl http://localhost:5000/plants -X POST -d '{"name": "Jasmine", "type": "Flower", "sellers": []}' -H "Content-Type: application/json"```

Create seller:
```curl http://localhost:5000/sellers -X POST -d '{"name": "Name200", "surname": "Surname200"}' -H "Content-Type: application/json"```

Add seller to plant's sellers list:
```curl http://localhost:5000/plants/{id}/sellers -X POST -d '{"id": {seller_id}, "name": "Name200", "surname": "Surname200"}' -H "Content-Type: application/json"```

### READ:
Read plants:
```curl -X GET http://localhost:5000/plants```

Read specific plant:
```curl -X GET http://localhost:5000/plants/{id}```

Read sellers:
```curl -X GET http://localhost:5000/sellers```

Read specific seller:
```curl -X GET http://localhost:5000/sellers/{id}```

Read plant's sellers:
```curl -X GET http://localhost:5000/plants/{id}/sellers```

Read plant's specific seller:
```curl -X GET http://localhost:5000/plants/{id}/sellers/{id}```

### UPDATE:
Update plant:
```curl -X PUT http://localhost:5000/plants/1 -d '{"name": "Red rose", "type": "Summer Flower", "sellers": []}' -H "Content-Type: application/json"```

Update seller:
```curl -X PUT http://localhost:5000/sellers/1 -d '{"name": "Nameful", "surname": "Known"}' -H "Content-Type: application/json"```

Update plant's seller:
```curl -X PUT http://localhost:5000/plants/2/sellers/2 -d '{"name": "NameName", "surname": "SurSurNameName"}' -H "Content-Type: application/json"```

### DELETE:
Delete plant:
```curl -X DELETE http://localhost:5000/plants/{id}```

Delete seller:
```curl -X DELETE http://localhost:5000/sellers/{id}```

Delete plant's seller:
```curl -X DELETE http://localhost:5000/plants/{id}/sellers/{id}```

