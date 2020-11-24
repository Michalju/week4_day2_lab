import pdb
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

# task_repository.delete_all()
# user_repository.delete_all()

artist_1 = Artist('Depeche Mode')
artist_repository.save(artist_1)
artist_2 = Artist('Metallica')
artist_repository.save(artist_2)

album_1 = Album('Teens of Denial', 'Rock', artist_1)
album_repository.save(album_1)
album_2 = Album('Ride The Lighting', 'Metal', artist_2)
album_repository.save(album_2)


pdb.set_trace()