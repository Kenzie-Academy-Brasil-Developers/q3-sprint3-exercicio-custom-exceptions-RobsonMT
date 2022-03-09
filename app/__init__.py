from flask import Flask, jsonify, request
from .services import read_csv, create_people
# Importe suas classes de exceções

app = Flask(__name__)

@app.get('/peoples')
def get_all():
    try:
        response = read_csv()

    except: # Chame a sua respectiva exceção criada 
        # retorne a respectiva mensagem 
        pass

    return jsonify(response)

@app.post('/peoples')
def register():
    data_body = request.get_json()

    try:
        create_people(data_body)

    except: # Chame a sua respectiva exceção criada 
        # retorne a respectiva mensagem 
        pass

    return {'success': 'People created!'}, 201