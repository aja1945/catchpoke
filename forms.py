from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class PokemonForm(FlaskForm):
    nickname = StringField('Nickname', render_kw={'readonly': True})
    submit = SubmitField('Catch Pokemon')
