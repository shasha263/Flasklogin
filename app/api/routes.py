from flask import Blueprint,jsonify,request
from app.models import Marvel_char,db
from flask_login import login_required 
from .apihelpers import token_required


api=Blueprint('api',__name__,url_prefix='/api')

@api.route('/')
def test():
    return {'datadatadata':'Fancy'}

@api.route('/marvelCharacters',methods=['GET'])
@login_required
def marvelcharacters():    
    marvelcharacters =[character.to_dict() for character in Marvel_char.query.all()]
    return jsonify(marvelcharacters)

@api.route('/marvelCharacters/<int:year>',methods=['GET'])
def get_number(year):
    marvelcharacters=Marvel_char.query.filter_by(comics_appeared_in	=year).all()
    if not marvelcharacters:
        return jsonify({year:None})
    return jsonify([x.to_dict() for x in marvelcharacters])

@api.route('/marvelCharacters/<string:nm>',methods=['GET'])
def get_name(nm):
    nm= nm.replace('_',' ').title()
    marvelcharacters=Marvel_char.query.filter_by(name=nm).all()
    if not marvelcharacters:
        return jsonify({nm:None})
    return jsonify([x.to_dict() for x in marvelcharacters])

@api.route('/createcharacter',methods=['POST'])   
@token_required
def createchar():
    data=request.get_json()
    print(data)
    checks= Marvel_char.query.filter_by(name=data['name']).all()
    if checks:  
        return jsonify({'Create Character rejected': 'Character already exists.'})
    newchar=Marvel_char()
    newchar.from_dict(data)
    db.session.add(newchar)
    db.session.commit()
    return jsonify({'Created':newchar.to_dict()})

@api.route('/update/<string:id>',methods=['PUT'])   
@token_required
def updatechar(id):
    data=request.get_json()
    print(data)
    character=Marvel_char.query.get(id)
    if not character:
        return jsonify({'Update failed': 'No character with that Id'})
    character.from_dict(data)
    print(character.to_dict())
    db.session.commit()
    return jsonify({'Updated':character.to_dict()})

@api.route('/delete/<string:id>',methods=['DELETE']) 
@token_required  
def deletechar(id):
    p=Marvel_char.query.get(id)
    if not p:
        return jsonify({'Delete failed':'No character of that ID exist'})
    db.session.delete(p)
    db.session.commit()
    return jsonify({'Deleted':p.to_dict()})

    




