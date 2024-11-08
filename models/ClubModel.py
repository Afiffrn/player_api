from config import db

class Club(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)

    # Relationship with the Player table
    players = db.relationship('Player', backref='club', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city,
            # Optionally include players if needed
            'players': [player.to_dict() for player in self.players] 
        }
