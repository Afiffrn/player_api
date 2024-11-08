from config import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    position = db.Column(db.String(50), nullable=False)
    club_id = db.Column(db.Integer, db.ForeignKey('club.id'), nullable=False)  # Corrected table reference

    stats = db.relationship('Stats', backref='player', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'position': self.position,
            'club_id': self.club_id,
            # Optionally include stats if needed
            'stats': [stat.to_dict() for stat in self.stats]
        }
