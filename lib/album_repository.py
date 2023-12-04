from lib.album import Album

class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection


    def all(self):
        # Return a list of Album objects from the db
        rows = self._connection.execute('SELECT * from albums')
        albums = []
        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        
        return albums
    
    def find(self, id):
        rows = self._connection.execute(
            'SELECT * from albums WHERE id=%s', [id])
        if rows:
            row = rows[0]
            return Album(row['id'], row['title'], row['release_year'], row['artist_id'])
        
    def create(self, name, release_year, artist_id):
        self._connection.execute(
            'INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)',
            [name, release_year, artist_id]
        )

    def delete(self, id):
        self._connection.execute(
            'DELETE FROM albums WHERE id = %s', [id]
        )