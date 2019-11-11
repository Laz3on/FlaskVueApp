from flask import Flask, jsonify, request
from flask_cors import CORS

# configuration
# change to false before spinning up to external web server
# TODO - MUST CHANGE TO FALSE BEFORE DEPLOY
DEBUG = True


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
# allows requests on all routes from any domain
# TODO - MUST CHANGE BEFORE DEPLOY
CORS(app, resources={r'/*': {'origins': '*'}})


BOOKS = [
    {
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]


# sanity check route
@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
