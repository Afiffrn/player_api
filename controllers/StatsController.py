from flask import jsonify, request
from models.PlayerModel import Player
from models.StatsModel import Stats
from config import db

def get_statser():
    statser = Stats.query.all()
    statser_with_players = []

    for stats in statser:
        player = Player.query.get(stats.player_id)
        statser_with_players.append({
            "id": stats.id,
            "player_name": player.name if player else "No player",
            "matches_played": stats.matches_played,
            "goals": stats.goals,
            "assists": stats.assists,
            "yellow_cards": stats.yellow_cards,
            "red_cards": stats.red_cards,
        })

    return jsonify(statser_with_players)

def get_stats(stats_id):
    stats = Stats.query.get(stats_id)

    if not stats:
        return jsonify({'status': 'error', 'message': 'stats not found'}), 404

    player = Player.query.get(stats.player_id)

    stats_data = {
        "id": stats.id,
        "player_name": player.name if player else "No player",
        "matches_played": stats.matches_played,
        "goals": stats.goals,
        "assists": stats.assists,
        "yellow_cards": stats.yellow_cards,
        "red_cards": stats.red_cards,
    }

    return jsonify(stats_data)

def add_stats():
    new_stats_data = request.get_json()

    new_stats = Stats(
        player_id=new_stats_data['player_id'],
        matches_played=new_stats_data['matches_played'],
        goals=new_stats_data['goals'],
        assists=new_stats_data['assists'],
        yellow_cards=new_stats_data.get('yellow_cards', 0),
        red_cards=new_stats_data.get('red_cards', 0),
    )

    db.session.add(new_stats)
    db.session.commit()

    return jsonify({'message': 'stats added successfully!', 'stats': new_stats.to_dict()}), 201

def update_stats(stats_id):
    stats = Stats.query.get(stats_id)

    if not stats:
        return jsonify({'error': 'stats not found'}), 404

    stats.matches_played = data.get('matches_played', stats.matches_played)
    stats.goals = data.get('goals', stats.goals)
    stats.assists = data.get('assists', stats.assists)
    stats.yellow_cards = data.get('yellow_cards', stats.yellow_cards)
    stats.red_cards = data.get('red_cards', stats.red_cards)
    db.session.commit()

    return jsonify({'message': 'stats updated successfully!', 'stats': stats.to_dict()})

def patch_stats(stats_id):
    stats = Stats.query.get(stats_id)

    if not stats:
        return jsonify({'error': 'stats not found'}), 404

    updated_data = request.get_json()

    if 'matches_played' in updated_data:
        stats.matches_played = updated_data['matches_played']
    if 'goals' in updated_data:
        stats.goals = updated_data['goals']
    if 'assists' in updated_data:
        stats.assists = updated_data['assists']
    if 'yellow_cards' in updated_data:
        stats.yellow_cards = updated_data['yellow_cards']
    if 'red_cards' in updated_data:
        stats.red_cards = updated_data['red_cards']

    db.session.commit()
    return jsonify({'message': 'stats updated successfully!', 'stats': stats.to_dict()})

def delete_stats(stats_id):
    stats = Stats.query.get(stats_id)

    if not stats:
        return jsonify({'error': 'stats not found'}), 404

    db.session.delete(stats)
    db.session.commit()
    return jsonify({'message': 'stats deleted successfully!'})
