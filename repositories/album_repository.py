from db.run_sql import run_sql
from models.album import Album

# CREATE TABLE albums (
#   id SERIAL PRIMARY KEY, -- Primary Key
#   artist_id INT REFERENCES artists(id), -- Foreign Key refs to artists table
#   title VARCHAR(255),  
#   genre VARCHAR(255)
# );

def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s,%s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

    