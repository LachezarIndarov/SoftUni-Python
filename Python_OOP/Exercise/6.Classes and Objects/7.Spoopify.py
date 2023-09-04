from project7.album import Album
from project7.band import Band
from project7.song import Song


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())


"""
output:

Running in the 90s - 3.45
Song Around the World has been added to the album Initial D.
Album Initial D
== Running in the 90s - 3.45
== Around the World - 2.34

Album Initial D has been published.
Band Manuel has added their newest album Initial D.
Album has been published. It cannot be removed.
Band Manuel
Album Initial D
== Running in the 90s - 3.45
== Around the World - 2.34

"""
