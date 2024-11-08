from flask import Blueprint
from controllers.StatsController import get_statser, get_stats, update_stats, patch_stats, delete_stats, add_stats

stats_bp = Blueprint('stats_bp', __name__)

# Route to get all stats
stats_bp.route('/api/stats', methods=['GET'])(get_statser)

# Route to get a specific stat
stats_bp.route('/api/stats/<int:stats_id>', methods=['GET'])(get_stats)

# Route to add a new stat
stats_bp.route('/api/stats', methods=['POST'])(add_stats)

# Route to update a specific stat (full update - PUT)
stats_bp.route('/api/stats/<int:stats_id>', methods=['PUT'])(update_stats)

# Route to update a specific stat (partial update - PATCH)
stats_bp.route('/api/stats/<int:stats_id>', methods=['PATCH'])(patch_stats)

# Route to delete a specific stat
stats_bp.route('/api/stats/<int:stats_id>', methods=['DELETE'])(delete_stats)
