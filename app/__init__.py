from http import HTTPStatus
from flask import Flask, jsonify, request
from .services import read_csv, create_people
# Importe suas classes de exceções

app = Flask(__name__)

@app.get('/peoples')
def get_all():
    try:
        response = read_csv()

    except ValueError: # Chame a sua respectiva exceção criada 
        # retorne a respectiva mensagem 
        return {"error": "The list is empty!"}, 404

    return jsonify(response), 200

@app.post('/peoples')
def register():
    data_body = request.get_json()
    cpf = data_body.get("cpf")

    try:
        create_people(data_body)

    except ValueError: # Chame a sua respectiva exceção criada 
        # retorne a respectiva mensagem 
        return {"error": f"CPF {cpf} already exists!"}, 409

    return {'success': 'People created!'}, 201