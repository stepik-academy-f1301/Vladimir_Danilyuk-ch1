from flask import Flask
from flask import render_template
from werkzeug import exceptions

errors = {
    404: "<h1>Страница не найдена</h1>",
    500: "<h1>Внутренняя ошибка сервера</h1>"
}

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/from/<direction>')
def get_direction(direction):
    return render_template('direction.html')


@app.route('/tours/<int:tour_id>')
def get_tour(tour_id):
    return render_template('tour.html')


@app.errorhandler(exceptions.NotFound)
def not_found(e):
    return errors[e.code], e.code


@app.errorhandler(exceptions.InternalServerError)
def server_error(e):
    return errors[e.code], e.code


if __name__ == '__main__':
    app.run()