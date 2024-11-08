from flask import jsonify, request
from models.PlayerModel import Player
from models.ClubModel import Club
from models.StatsModel import Stats
from config import db

def get_players():
    players = Player.query.all()
    players_with_clubs = []

    for player in players:
        club = Club.query.get(player.club_id)
        players_with_clubs.append({
            'id': player.id,
            'name': player.name,
            'age': player.age,
            'position': player.position,
            'club_name': club.name if club else "No club"
        })

    return jsonify(players_with_clubs)

def get_player(player_id):
    player = Player.query.get(player_id)

    if not player:
        return jsonify({'status': 'error', 'message': 'player not found'}), 404

    club = Club.query.get(player.club_id)

    player_data = {
        "id": player.id,
        "name": player.name,
        "age": player.age,
        "position": player.position,
        "club": club.name if club else "No club"
    }

    return jsonify(player_data)

def add_player():
    new_player_data = request.get_json()

    new_player = Player(
        name=new_player_data['name'],
        age=new_player_data['age'],
        position=new_player_data['position'],
        club_id=new_player_data['club_id']
    )

    db.session.add(new_player)
    db.session.commit()

    return jsonify({'message': 'player added successfully!', 'player': new_player.to_dict()}), 201


def update_player(player_id):
    player = Player.query.get(player_id)

    if not player:
        return jsonify({'error': 'player not found'}), 404

    updated_data = request.get_json()

    player.name = updated_data.get('name', player.name)
    player.age = updated_data.get('age', player.age)
    player.position = updated_data.get('position', player.position)
    player.club_id = updated_data.get('club_id', player.club_id)

    db.session.commit()
    return jsonify({'message': 'player updated successfully!', 'player': player.to_dict()})

def patch_player(player_id):
    player = Player.query.get(player_id)

    if not player:
        return jsonify({'error': 'player not found'}), 404

    updated_data = request.get_json()

    if 'name' in updated_data:
        player.name = updated_data['name']
    if 'age' in updated_data:
        player.age = updated_data['age']
    if 'position' in updated_data:
        player.position = updated_data['position']
    if 'club_id' in updated_data:
        club = Club.query.get(updated_data['club_id'])  # Use Club model here
        if club:
            player.club_id = updated_data['club_id']
        else:
            return jsonify({'error': 'club not found'}), 404

    db.session.commit()
    return jsonify({'message': 'player updated successfully!', 'player': player.to_dict()})

def delete_player(player_id):
    player = Player.query.get(player_id)

    if not player:
        return jsonify({'error': 'player not found'}), 404

    db.session.delete(player)
    db.session.commit()
    return jsonify({'message': 'player deleted successfully!'})
