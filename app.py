import os
from flask import Flask, request
from lib.database_connection import DatabaseConnection
from lib.album import Album
from lib.album_repository import AlbumRepository
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)



# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

@app.route('/albums', methods=['POST'])
def create_album():
    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']
    connection = get_flask_database_connection(app)
    album_repo = AlbumRepository(connection)
    album_repo.create(title, release_year, artist_id)
    return 'Album added successfully'

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    album_repo = AlbumRepository(connection)
    albums = album_repo.all()
    return '\n'.join(str(album) for album in albums)

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

