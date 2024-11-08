from config import db

class Stats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)  # Corrected table reference
    matches_played = db.Column(db.Integer, nullable=False)
    goals = db.Column(db.Integer, nullable=False)
    assists = db.Column(db.Integer, nullable=False)
    yellow_cards = db.Column(db.Integer, nullable=True, default=0)
    red_cards = db.Column(db.Integer, nullable=True, default=0)

    def to_dict(self):
        return {
            'id': self.id,
            'player_id': self.player_id,
            'matches_played': self.matches_played,
            'goals': self.goals,
            'assists': self.assists,
            'yellow_cards': self.yellow_cards,
            'red_cards': self.red_cards
        }
