import pdb
from models.artist import Artist

import repositories.artist_repository as artist_repository


# task_repository.delete_all()
# user_repository.delete_all()

Artist1 = Artist('Depeche Mode')
artist_repository.save(Artist1)
Artist2 = Artist('Metallica')
artist_repository.save(Artist2)

pdb.set_trace()