from flask import jsonify, request
from models.ClubModel import Club
from config import db

def get_clubs():
    clubs = Club.query.all()
    return jsonify([club.to_dict() for club in clubs])

def get_club(club_id):
    club = Club.query.get(club_id)
    if not club:
        return jsonify({'error': 'club not found'}), 404
    return jsonify(club.to_dict())

def add_club():
    new_club_data = request.get_json()
    new_club = Club(name=new_club_data['name'], city=new_club_data['city'])  # Fixed typo here
    db.session.add(new_club)
    db.session.commit()
    return jsonify({'message': 'club added successfully!', 'club': new_club.to_dict()}), 201

def update_club(club_id):
    club = Club.query.get(club_id)
    if not club:
        return jsonify({'error': 'club not found'}), 404
    updated_data = request.get_json()
    club.name = updated_data.get('name', club.name)
    club.city = updated_data.get('city', club.city)  # Fixed typo here
    db.session.commit()
    return jsonify({'message': 'club updated successfully!', 'club': club.to_dict()})

def delete_club(club_id):
    club = Club.query.get(club_id)
    if not club:
        return jsonify({'error': 'club not found'}), 404
    db.session.delete(club)
    db.session.commit()
    return jsonify({'message': 'club deleted successfully!'})
