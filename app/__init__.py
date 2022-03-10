from tkinter import E
from flask import Flask, jsonify, request
from .services import read_csv, create_people
from .exc import EmptyListError, CpfExistError

app = Flask(__name__)

@app.get('/peoples')
def get_all():
    try:
        response = read_csv()

    except EmptyListError as err:
        return err.message, 404

    return jsonify(response)

@app.post('/peoples')
def register():
    data_body = request.get_json()

    try:
        create_people(data_body)

    except CpfExistError as err:
        return err.message, 409

    return {'sucess': 'People created!'}, 201