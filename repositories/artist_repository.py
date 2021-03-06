from db.run_sql import run_sql
from models.artist import Artist
import repositories.album_repository as album_repository
def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def delete_all():
    sql = "DELETE  FROM artists" 
    run_sql(sql)

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"  
    values = [id] 
    result = run_sql(sql, values)[0]
    
    if result is not None:
        artist = Artist(result['name'], result['id'] )
    return artist

def select_all():  
    artists = [] 

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row['name'], row['id'] )
        artists.append(artist)
    return artists

def edit_name(old_name, new_name):
    sql = "UPDATE artists SET name = (%s) WHERE name = (%s) RETURNING * "
    values = [new_name, old_name]
    result = run_sql(sql, values)
    if not result:
        print(f"!!!!!!!! Can't find artist {old_name}") 

def delete_by_id(id):
    #First need to delete all albums associated with the artist
    sql = "DELETE  FROM albums WHERE artist_id = %s" 
    values = [id]
    run_sql(sql, values)

    sql = "DELETE  FROM artists WHERE id = %s" 
    values = [id]
    run_sql(sql, values)