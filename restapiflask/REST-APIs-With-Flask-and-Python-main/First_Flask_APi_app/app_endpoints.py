from flask import Flask, jsonify

app_endpoints = Flask(__name__)


stores = [

    {
        
        'name': "My Initial Store",
        'items': [
            
            {
                'name': "My Items",
                'price' : 150 
            
            }
        ]

    }
    
]


# POST - used to receive data
# Get - used to send data back only

# POST /store data: (name:)
@app_endpoints.route('/store', methods=['POST'])
def create_store():
    pass

# GET /store/<string:name>
app_endpoints.route('/store/<string:name>') # 'https//127.0.0.1:5000/store/some_name
def get_store(name):
    pass

# GET/store
@app_endpoints.route('/store')
def get_stores():
    return jsonify({'stores' : stores})

# POST /store/<string:name>/item (name:, price:)
@app_endpoints.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass


# GET /store/<string:name>/item
app_endpoints.route('/store/<string:name>/item') 
def get_item_in_store(name):
    pass

app_endpoints.run(port=5000)