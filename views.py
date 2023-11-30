from flask import render_template, redirect, url_for, flash
from .models import User, Pokemon, UserPokemon
from .forms import PokemonForm
from flask_login import current_user, login_required

@app.route('/catch_pokemon/<int:pokemon_id>', methods=['GET', 'POST'])
@login_required
def catch_pokemon(pokemon_id):
    form = PokemonForm()
    pokemon = Pokemon.query.get_or_404(pokemon_id)

    if form.validate_on_submit():
        if current_user.can_catch_pokemon():
            user_pokemon = UserPokemon(user=current_user, pokemon=pokemon, nickname=form.nickname.data)
            db.session.add(user_pokemon)
            db.session.commit()
            flash(f'You caught {pokemon.name}!', 'success')
            return redirect(url_for('pokemon_list'))
        else:
            flash('You have already reached the maximum number of Pokemon in your collection.', 'error')

    return render_template('catch_pokemon.html', form=form, pokemon=pokemon)
