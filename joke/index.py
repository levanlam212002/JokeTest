

from flask import render_template, session, request

from joke import app, models, db
from joke.models import Joke


@app.route("/")
def index():
    joke = models.Joke.query.filter_by(status=0).first()
    return render_template('index.html', joke=joke)


@app.route("/funny/<int:joke_id>", methods=['GET', 'POST'])
def funny(joke_id):
    if request.method.__eq__('POST'):
        Joke.query.filter_by(id=joke_id).first().status = 1
        db.session.commit()
    joke = models.Joke.query.filter_by(status=0).first()
    return render_template('index.html', joke=joke)


if __name__ == '__main__':
    app.run(debug=True)
