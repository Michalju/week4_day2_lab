import pdb
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

# Task 1
# artist_1 = Artist('Depeche Mode')
# artist_repository.save(artist_1)
# artist_2 = Artist('Metallica')
# artist_repository.save(artist_2)


# Task 2
# album_1 = Album('Teens of Denial', 'Rock', artist_1)
# album_repository.save(album_1)
# album_2 = Album('Ride The Lighting', 'Metal', artist_2)
# album_repository.save(album_2)


#Task 3
# album_repository.delete_all()
# artist_repository.delete_all()

#Task 4 & 5
# artist_1 = Artist('AC/DC')
# artist_2 = Artist('Metallica')
# artist_repository.save(artist_1)
# artist_repository.save(artist_2)

# album_1 = Album('High Voltage', 'Rock', artist_1)
# album_2 = Album('Dirty Deeds Done Dirt Cheap', 'Rock', artist_1)
# album_3 = Album('Let There Be Rock', 'Rock', artist_1)
# album_4 = Album('Highway to Hell', 'Rock', artist_1)
# album_5 = Album('Back in Black', 'Rock', artist_1)

# album_6 = Album('Kill Them All', 'Metal', artist_2)
# album_7 = Album('Ride the Lighting', 'Metal', artist_2)
# album_8 = Album('Master Of Puppets', 'Metal', artist_2)
# album_9 = Album('And Justice For All', 'Metal', artist_2)
# album_10 = Album('Metallica', 'Metal', artist_2)

# album_repository.save(album_1)
# album_repository.save(album_2)
# album_repository.save(album_3)
# album_repository.save(album_4)
# album_repository.save(album_5)
# album_repository.save(album_6)
# album_repository.save(album_7)
# album_repository.save(album_8)
# album_repository.save(album_9)
# album_repository.save(album_10)

# Extension task 1
# album_repository.list_albums_by_artist_id(20)
# album_repository.list_albums_by_artist_name("AC/DC")

# Extension task 2
# old_title = "High Voltage"
# new_title = "Very High Voltage"
# album_repository.list_albums_by_artist_name("AC/DC")
# album_repository.edit_title(old_title, new_title)
# album_repository.list_albums_by_artist_name("AC/DC")
# album_repository.edit_title(new_title, old_title)
# album_repository.list_albums_by_artist_name("AC/DC")

# old_artist_name = "Metallica"
# new_artist_name = "Megadeath"
# print(f"Artist name BEFORE change: {artist_repository.select(20).name}")
# artist_repository.edit_name(old_artist_name, new_artist_name)
# print(f"Artist name AFTER change: {artist_repository.select(20).name}")
# artist_repository.edit_name(new_artist_name, old_artist_name)
# print(f"Artist name back to how it was: {artist_repository.select(20).name}")

# Extension task 3
# artist_repository.delete_by_id(20)
# album_repository.delete_by_id(60)
#pdb.set_trace()