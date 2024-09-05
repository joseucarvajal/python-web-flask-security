from flask import Flask, request, jsonify
import os

class User:
    def __init__(self, user_name, email, password):
        self.user_name = user_name
        self.email = email
        self.password = password

app = Flask(__name__)

@app.route('/create_user', methods=['POST'])
def create_person():
    data = request.json
    
    user = User(user_name=data['user_name'] + "cambiado", email=data['email'], password=data['password'])
    
    #return jsonify(user.__dict__)
    return jsonify({
        "data": "hola", 
    })

@app.route('/echo', methods=['GET'])
def echo():
    param = request.args.get('param', default='', type=str)
    return jsonify({'response': param})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)
