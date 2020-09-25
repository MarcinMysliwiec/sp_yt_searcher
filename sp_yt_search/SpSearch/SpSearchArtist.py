from .Sp import Sp
from .SpSearchAlbum import SpSearchAlbum
from .objects.GenericArtistObj import GenericArtistObj


class SpSearchArtist(Sp):
    def __init__(self, artist_id):
        self.artist_id = artist_id
        super(SpSearchArtist, self).__init__()

    def search(self):
        artist = self.client.artist(self.artist_id)
        artist_albums = self.client.artist_albums(self.artist_id)
        artist['albums'] = list()
        while True:
            for item in artist_albums['items']:
                artist['albums'].append(SpSearchAlbum(item['id']))

            if artist_albums['next'] is None:
                break
            artist_albums = self.client.next(artist_albums)

        self.obj = artist

    def to_generic(self):
        generic = self.obj
        for ite, album in enumerate(generic['albums']):
            generic['albums'][ite] = album.to_generic()

        return GenericArtistObj(generic).__dict__

    def to_artist(self):
        return self.to_generic()
