import pdb
from models.artist import Artist

import repositories.artist_repository as artist_repository


# task_repository.delete_all()
# user_repository.delete_all()

Artist1 = User('Depeche Mode')
artist_repository.save(Artist1)
Artist2 = User('Metallica')
artist_repository.save(Artist2)

pdb.set_trace()