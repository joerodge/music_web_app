# Tests for your routes go here

# === Example Code Below ===
from lib.album_repository import AlbumRepository
from lib.album import Album

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"


def test_create_a_new_album(web_client, db_connection):
    db_connection.seed('seeds/music.sql')
    album_repo = AlbumRepository(db_connection)
    response = web_client.post("/albums",data={'title': 'Voyage','release_year': 2022,'artist_id': 2})
    assert response.data.decode('utf-8') == 'Album added successfully'
    albums = album_repo.all()

    assert albums == [
        Album(1,'Doolittle', 1989, 1),
        Album(2,'Surfer Rosa', 1988, 1),
        Album(3,'Waterloo', 1974, 2),
        Album(4,'Super Trouper', 1980, 2),
        Album(5,'Bossanova', 1990, 1),
        Album(6,'Lover', 2019, 3),
        Album(7,'Folklore', 2020, 3),
        Album(8,'I Put a Spell on You', 1965, 4),
        Album(9,'Baltimore', 1978, 4),
        Album(10,'Here Comes the Sun', 1971, 4),
        Album(11,'Fodder on My Wings', 1982, 4),
        Album(12,'Ring Ring', 1973, 2),
        Album(13, 'Voyage', 2022, 2)
    ]

def test_create_a_new_album_assert_with_GET(web_client, db_connection):
    db_connection.seed('seeds/music.sql')
    res = web_client.post("/albums",data={'title': 'Voyage','release_year': 2022,'artist_id': 2})
    assert res.data.decode('utf-8') == 'Album added successfully'
    response = web_client.get("/albums")
    assert response.data.decode('utf-8') == '\n'.join([
        "Album(1, Doolittle, 1989, 1)",
        "Album(2, Surfer Rosa, 1988, 1)",
        "Album(3, Waterloo, 1974, 2)",
        "Album(4, Super Trouper, 1980, 2)",
        "Album(5, Bossanova, 1990, 1)",
        "Album(6, Lover, 2019, 3)",
        "Album(7, Folklore, 2020, 3)",
        "Album(8, I Put a Spell on You, 1965, 4)",
        "Album(9, Baltimore, 1978, 4)",
        "Album(10, Here Comes the Sun, 1971, 4)",
        "Album(11, Fodder on My Wings, 1982, 4)",
        "Album(12, Ring Ring, 1973, 2)",
        "Album(13, Voyage, 2022, 2)",
    ])

def test_artist_get(web_client, db_connection):
    db_connection.seed('seeds/music.sql')
    response = web_client.get('/artists')
    assert response.status == '200 OK'
    assert response.data.decode('utf-8') == 'Pixies, ABBA, Taylor Swift, Nina Simone'

def test_add_artist(web_client, db_connection):
    db_connection.seed('seeds/music.sql')
    response = web_client.post('/artists', data = {'name': 'Wild nothing', 'genre': 'Indie'})
    assert response.status == '200 OK'
    response = web_client.get('/artists')
    assert response.status == '200 OK'
    assert response.data.decode('utf-8') == 'Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing'