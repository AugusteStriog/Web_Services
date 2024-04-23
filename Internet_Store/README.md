Internet Store

To launch web service:

`git clone`
`cd Internet_Store`
`docker build -t app .`
`docker run -p 5000:5000 app`

Use postman to test HTTP methods:
`https://www.postman.com/downloads/`

#GET
READ
Get all items:
`curl -X GET http://localhost:5000/items`
Get all users:
`curl -X GET http://localhost:5000/users`
Get all shops:
`curl -X GET http://localhost:5000/shops`
Get specific item:
`curl -X GET http://localhost:5000/items/2`
Get specific user:
`curl -X GET http://localhost:5000/users/1`
Get specific shop:
`curl -X GET http://localhost:5000/shops/1`

#POST
CREATE
Create an item
`curl -X POST http://localhost:5000/items -H "Content-Type: application/json" -d '{"title": "New Item", "manufacturer": "New Manufacturer"}'`
Create a user:
`curl -X POST http://localhost:5000/users -H "Content-Type: application/json" -d '{"name": "John Smith"}'`
Create a shop:
`curl -X POST http://localhost:5000/shops -H "Content-Type: application/json" -d '{"address": "123 Main St"}'`

#PUT
UPDATE
Upadate an item:
`curl -X PUT http://localhost:5000/items/1 -H "Content-Type: application/json" -d '{"title": "Updated Item", "manufacturer": "Updated Manufacturer"}'`
Update a user:
`curl -X PUT http://localhost:5000/users/1 -H "Content-Type: application/json" -d '{"name": "Updated Name"}'`
Update a shop:
`curl -X PUT http://localhost:5000/shops/1 -H "Content-Type: application/json" -d '{"address": "Updated Address"}'`
Assign user to an item:
`curl -X PUT http://localhost:5000/items/1/assign/user/1`
Assign item to a shop:
`curl -X PUT http://localhost:5000/items/1/assign/shop/1`

#DELETE
DELETE
Delete an item:
`curl -X DELETE http://localhost:5000/items/1`
Delete a user:
`curl -X DELETE http://localhost:5000/users/2`
Delete a shop:
`curl -X DELETE http://localhost:5000/shops/1`
Unasign user from an item:
`curl -X DELETE http://localhost:5000/items/1/unassign/user`
Unasign item from a shop:
`curl -X DELETE http://localhost:5000/items/1/unassign/shop`
