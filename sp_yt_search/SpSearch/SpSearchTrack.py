from .Sp import Sp
from .objects.GenericArtistObj import GenericArtistObj
from .objects.GenericAlbumObj import GenericAlbumObj
from .objects.GenericTrackObj import GenericTrackObj


class SpSearchTrack(Sp):
    def __init__(self, track_id):
        self.track_id = track_id
        super(SpSearchTrack, self).__init__()

    def search(self):
        self.obj = self.client.track(self.track_id)

    def to_generic(self):
        return GenericTrackObj(self.obj).__dict__

    def to_artist(self):
        return GenericArtistObj({
            'id': self.obj['artists'][0]['id'],
            'uri': self.obj['artists'][0]['uri'],
            'name': self.obj['artists'][0]['name'],
            'albums': [GenericAlbumObj({
                'id': self.obj['album']['id'],
                'uri': self.obj['album']['uri'],
                'name': self.obj['album']['name'],
                'label': '',
                'release_date': self.obj['album']['release_date'],
                'total_tracks': self.obj['album']['total_tracks'],
                'tracks': self.to_generic()
            }).__dict__],
        }).__dict__
