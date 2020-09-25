from .Sp import Sp
from .objects.GenericAlbumObj import GenericAlbumObj
from .objects.GenericTrackObj import GenericTrackObj


class SpSearchAlbum(Sp):
    def __init__(self, album_id):
        self.album_id = album_id
        super(SpSearchAlbum, self).__init__()

    def search(self):
        album = self.client.album(self.album_id)
        album_tracks = self.client.album_tracks(self.album_id)
        album['tracks'] = list()

        while True:
            album['tracks'].extend(album_tracks['items'])
            if album_tracks['next'] is None:
                break
            album_tracks = self.client.next(album_tracks)

        if len(album['tracks']) != album['total_tracks']:
            raise Exception('To Do')

        self.obj = album

    def to_generic(self):
        data = self.obj
        for ite, track in enumerate(data['tracks']):
            data['tracks'][ite] = GenericTrackObj(track).__dict__

        self.generic_data = GenericAlbumObj(data).__dict__
