from db.run_sql import run_sql
from models.album import Album
import repositories.artist_repository as artist_repository

def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s,%s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def delete_all():
    sql = "DELETE  FROM albums" 
    run_sql(sql)

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = (%s)"  
    values = [id] 
    result = run_sql(sql, values)[0]
    
    if result is not None:
        artist = artist_repository.select(result['artist_id'])
        album = Album(result['title'], result['genre'], artist, result['id'])
    return album

def select_all():  
    albums = [] 

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(row['title'],row['genre'], artist, row['id'] )
        albums.append(album)
    return albums

def list_albums_by_artist_id(id):
    sql = "SELECT * FROM albums WHERE artist_id = (%s)"  
    values = [id] 
    results = run_sql(sql, values)
    if results :
        print (f"Album made by {artist_repository.select(id).name} :")
        print ("--------------------------------------")
        for row in results:
            print (f"Album title = {row['title']}")
            print (f"Genre = {row['genre']}") 
            print ("--------------------------------------")
    else:
        print(f"!!!!!!!! Artist id {id} not found !!!!!!!!")

def list_albums_by_artist_name(name):
    sql = "SELECT id FROM artists WHERE name = (%s)"  
    values = [name] 
    results = run_sql(sql, values)
    if results:
        list_albums_by_artist_id(results[0]['id'])
    else:
        print(f"!!!!!!!! Artist {name} not found !!!!!!!!")