from lib.album import Album
from lib.album_repository import AlbumRepository

def test_get_all_albums(db_connection):
    db_connection.seed("seeds/music.sql")
    repository = AlbumRepository(db_connection)
    albums = repository.all()

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
    ]


def test_find_by_id(db_connection):
    db_connection.seed("seeds/music.sql")
    repository = AlbumRepository(db_connection)
    assert repository.find(3) == Album(3,'Waterloo', 1974, 2)

def test_find_by_id_doesnt_exist(db_connection):
    db_connection.seed("seeds/music.sql")
    repository = AlbumRepository(db_connection)
    assert repository.find(57) == None


def test_create_a_new_album(db_connection):
    db_connection.seed("seeds/music.sql")
    repository = AlbumRepository(db_connection)
    repository.create('Voyage', 2021, 2)
    albums = repository.all()

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
        Album(13, 'Voyage', 2021, 2)
    ]

def test_deleting_an_album(db_connection):
    db_connection.seed("seeds/music.sql")
    repository = AlbumRepository(db_connection)
    repository.delete(3)
    albums = repository.all()

    assert albums == [
        Album(1,'Doolittle', 1989, 1),
        Album(2,'Surfer Rosa', 1988, 1),
        Album(4,'Super Trouper', 1980, 2),
        Album(5,'Bossanova', 1990, 1),
        Album(6,'Lover', 2019, 3),
        Album(7,'Folklore', 2020, 3),
        Album(8,'I Put a Spell on You', 1965, 4),
        Album(9,'Baltimore', 1978, 4),
        Album(10,'Here Comes the Sun', 1971, 4),
        Album(11,'Fodder on My Wings', 1982, 4),
        Album(12,'Ring Ring', 1973, 2),
    ]

def test_deleting_a_record_that_doesnt_exist(db_connection):
    db_connection.seed("seeds/music.sql")
    repository = AlbumRepository(db_connection)
    repository.delete(37)
    albums = repository.all()

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
    ]