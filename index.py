from config import app, db
from routes.Player_bp import player_bp
from routes.Club_bp import club_bp
from routes.Stats_bp import stats_bp

app.register_blueprint(player_bp)
app.register_blueprint(club_bp)
app.register_blueprint(stats_bp)

# Remove the `if __name__ == '__main__':` block
# and run the app with WSGI server
with app.app_context():
	db.create_all()
#if __name__ == "__main__":
#    app.run()

