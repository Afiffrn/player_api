from flask import Blueprint
from controllers.PlayerController import get_players, get_player, update_player, patch_player, delete_player, add_player

player_bp = Blueprint('player_bp', __name__)

# Route to get all players
player_bp.route('/api/players', methods=['GET'])(get_players)

# Route to get a specific player
player_bp.route('/api/players/<int:player_id>', methods=['GET'])(get_player)

# Route to add a new player
player_bp.route('/api/players', methods=['POST'])(add_player)

# Route to update a specific player (full update - PUT)
player_bp.route('/api/players/<int:player_id>', methods=['PUT'])(update_player)

# Route to update a specific player (partial update - PATCH)
player_bp.route('/api/players/<int:player_id>', methods=['PATCH'])(patch_player)

# Route to delete a specific player
player_bp.route('/api/players/<int:player_id>', methods=['DELETE'])(delete_player)
