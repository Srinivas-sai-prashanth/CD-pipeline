from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data
data = {
    '1': {'name': 'John', 'age': 30},
    '2': {'name': 'Jane', 'age': 25}
}

# GET operation - Retrieve all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)

# GET operation - Retrieve a specific item by ID
@app.route('/items/<item_id>', methods=['GET'])
def get_item(item_id):
    item = data.get(item_id)
    if item:
        return jsonify(item)
    else:
        return jsonify({'error': 'Item not found'}), 404

# POST operation - Create a new item
@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.get_json()
    item_id = str(len(data) + 1)
    data[item_id] = new_item
    return jsonify({'id': item_id}), 201

# PUT operation - Update an existing item by ID
@app.route('/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    item = data.get(item_id)
    if item:
        updated_item = request.get_json()
        item.update(updated_item)
        return jsonify({'message': 'Item updated successfully'})
    else:
        return jsonify({'error': 'Item not found'}), 404

# DELETE operation - Delete an item by ID
@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = data.pop(item_id, None)
    if item:
        return jsonify({'message': 'Item deleted successfully'})
    else:
        return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

