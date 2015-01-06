from app import app, db
from app.models import myentity
from flask import abort, jsonify, request
import datetime
import json

@app.route('/myapp/myentities', methods = ['GET'])
def get_all_myentities():
    entities = myentity.Myentity.query.all()
    return json.dumps([entity.to_dict() for entity in entities])

@app.route('/myapp/myentities/<int:id>', methods = ['GET'])
def get_myentity(id):
    entity = myentity.Myentity.query.get(id)
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())

@app.route('/myapp/myentities', methods = ['POST'])
def create_myentity():
    entity = myentity.Myentity(
        myattr = request.json['myattr']
    )
    db.session.add(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201

@app.route('/myapp/myentities/<int:id>', methods = ['PUT'])
def update_myentity(id):
    entity = myentity.Myentity.query.get(id)
    if not entity:
        abort(404)
    entity = myentity.Myentity(
        myattr = request.json['myattr'],
        id = id
    )
    db.session.merge(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 200

@app.route('/myapp/myentities/<int:id>', methods = ['DELETE'])
def delete_myentity(id):
    entity = myentity.Myentity.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 204
