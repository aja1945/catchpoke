from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):

class Pokemon(db.Model):

class UserPokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemon.id'), nullable=False)
    nickname = db.Column(db.String(50)) 

    user = db.relationship('User', backref=db.backref('user_pokemons', lazy=True))
    pokemon = db.relationship('Pokemon', backref=db.backref('user_pokemons', lazy=True))

class User(db.Model):

    def can_catch_pokemon(self):
        return len(self.user_pokemons) < 5
