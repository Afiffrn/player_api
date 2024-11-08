from flask import Blueprint
from controllers.ClubController import get_clubs, get_club, update_club, delete_club, add_club

club_bp = Blueprint('club_bp', __name__)  # Add __name__ for consistency

# Route to get all clubs
club_bp.route('/api/clubs', methods=['GET'])(get_clubs)

# Route to get a specific club
club_bp.route('/api/clubs/<int:club_id>', methods=['GET'])(get_club)

# Route to add a new club
club_bp.route('/api/clubs', methods=['POST'])(add_club)

# Route to update a specific club
club_bp.route('/api/clubs/<int:club_id>', methods=['PUT'])(update_club)

# Route to delete a specific club
club_bp.route('/api/clubs/<int:club_id>', methods=['DELETE'])(delete_club)
