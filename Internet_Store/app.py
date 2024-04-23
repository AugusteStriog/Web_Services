from flask import Flask, request, jsonify
from items import Item, items
from users import User, users
from shops import Shop, shops

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'items': [item.__dict__ for item in items],
        'users': [user.__dict__ for user in users],
        'shops': [shop.__dict__ for shop in shops]
    })
    
#GET requests
@app.get('/items')
def get_all_items():
    return jsonify([item.__dict__ for item in items])

@app.get('/users')
def get_all_users():
    return jsonify([user.__dict__ for user in users])

@app.get('/shops')
def get_all_shops():
    return jsonify([shop.__dict__ for shop in shops])

# Get a specific item with ID
@app.get('/items/<int:item_id>')
def get_item_by_id(item_id):
    for item in items:
        if item.id == item_id:
            return jsonify(item.__dict__)
    return jsonify({'error': 'Item not found'}), 404

# Get a specific user with ID
@app.get('/users/<int:user_id>')
def get_user_by_id(user_id):
    for user in users:
        if user.id == user_id:
            return jsonify(user.__dict__)
    return jsonify({'error': 'Item not found'}), 404

# Get a specific shop with ID
@app.get('/shops/<int:shop_id>')
def get_shop_by_id(shop_id):
    for shop in shops:
        if shop.id == shop_id:
            return jsonify(shop.__dict__)
    return jsonify({'error': 'Item not found'}), 404

#Create an item
@app.post('/items')
def create_item():
    if not request.json or not 'title' in request.json or not 'manufacturer' in request.json:
        return jsonify({'error': 'Missing data for item creation'}), 400
    new_id = max(item.id for item in items) + 1 if items else 1
    new_item = Item(id=new_id, 
                    title=request.json['title'], 
                    manufacturer=request.json['manufacturer'],)    
    items.append(new_item)  
    return jsonify(new_item.__dict__), 201

#Create a user
@app.post('/users')
def create_user():
    if not request.json or not 'name' in request.json:
        return jsonify({'error': 'Missing name for user creation'}), 400
    new_id = max(user.id for user in users) + 1 if users else 1
    new_user = User(id=new_id, name=request.json['name'])
    users.append(new_user)
    return jsonify(new_user.__dict__), 201

#Create a shop
@app.post('/shops')
def create_shop():
    if not request.json or not 'address' in request.json:
        return jsonify({'error': 'Missing address for shop creation'}), 400
    new_id = max(shop.id for shop in shops) + 1 if shops else 1
    new_shop = Shop(id=new_id, address=request.json['address'])
    shops.append(new_shop)
    return jsonify(new_shop.__dict__), 201

#Assign item to user
@app.put('/items/<int:item_id>/user/<int:user_id>')
def assign_item_user(item_id, user_id):
    item = next((item for item in items if item.id == item_id), None)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    
    user = next((user for user in users if user.id == user_id), None)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    item.buyer_id = user_id
    return '', 204


#Assign item to a shop
@app.put('/items/<int:item_id>/shop/<int:shop_id>')
def assign_item_shop(item_id, shop_id):
    item = next((item for item in items if item.id == item_id), None)
    if not item:
        return jsonify({'error': 'Item not found'}), 404

    shop = next((shop for shop in shops if shop.id == shop_id), None)
    if not shop:
        return jsonify({'error': 'Shop not found'}), 404

    item.shop_id = shop_id
    return '', 204

#Update an item
@app.put('/items/<int:item_id>')
def update_item(item_id):
    item = next((item for item in items if item.id == item_id), None)
    
    if item is None:
        return jsonify({'error': 'Item not found'}), 404

    data = request.json
    title = data.get('title')
    manufacturer = data.get('manufacturer')

    if title is not None:
        item.title = title
    if manufacturer is not None:
        item.manufacturer = manufacturer

    return jsonify(item.__dict__), 200

#Update user
@app.put('/users/<int:user_id>')
def update_user(user_id):
    user = next((user for user in users if user.id == user_id), None)
    
    if user is None:
        return jsonify({'error': 'User not found'}), 404

    data = request.json
    name = data.get('name')

    if name is not None:
        user.name = name
    else:
        return jsonify({'error': 'No name provided for update'}), 400

    return jsonify(user.__dict__), 200

#Update shop
@app.put('/shops/<int:shop_id>')
def update_shop(shop_id):
    shop = next((shop for shop in shops if shop.id == shop_id), None)
    
    if shop is None:
        return jsonify({'error': 'Shop not found'}), 404

    data = request.json
    address = data.get('address')

    if address is not None:
        shop.address = address
    else:
        return jsonify({'error': 'No address provided for update'}), 400

    return jsonify(shop.__dict__), 200

#Delete item
@app.delete('/items/<int:item_id>')
def delete_item(item_id):
    item_index = next((index for index, item in enumerate(items) if item.id == item_id), None)
    
    if item_index is None:
        return jsonify({'error': 'Item not found'}), 404

    del items[item_index]

    return '', 204

#Delete user    
@app.delete('/users/<int:user_id>')
def delete_user(user_id):
    user_index = next((index for index, user in enumerate(users) if user.id == user_id), None)
    
    if user_index is None:
        return jsonify({'error': 'User not found'}), 404

    del users[user_index]

    return '', 204

#Delete shop
@app.delete('/shops/<int:shop_id>')
def delete_shop(shop_id):
    shop_index = next((index for index, shop in enumerate(shops) if shop.id == shop_id), None)
    
    if shop_index is None:
        return jsonify({'error': 'Shop not found'}), 404

    del shops[shop_index]

    return '', 204


#Unassign item from user
@app.delete('/items/<int:item_id>/user/<int:user_id>')
def clear_user_from_item(item_id, user_id):
    item = next((item for item in items if item.id == item_id), None)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    
    if item.buyer_id != user_id:
        return jsonify({'error': 'Item unassigned to the user'}), 404
   
    item.buyer_id = None
    return '', 204


#Unassign item from shop
@app.delete('/items/<int:item_id>/shop/<int:shop_id>')
def unassign_item_from_shop(item_id, shop_id):
    item = next((item for item in items if item.id == item_id), None)
    if not item:
        return jsonify({'error': 'Item not found'}), 404

    if item.shop_id != shop_id:
        return jsonify({'error': 'Item not unassigned to the shop'}), 404

    item.shop_id = None  
    return '', 204



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
