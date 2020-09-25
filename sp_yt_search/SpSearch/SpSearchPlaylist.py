from .Sp import Sp
from .objects.GenericPlaylistObj import GenericPlaylistObj
from .objects.GenericTrackObj import GenericTrackObj


class SpSearchPlaylist(Sp):
    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        super(SpSearchPlaylist, self).__init__()

    def search(self):
        playlist = self.client.playlist(self.playlist_id)
        playlist['total_tracks'] = playlist['tracks']['total']
        playlist['tracks'] = list()
        response = self.client.playlist_tracks(self.playlist_id)

        while True:
            playlist['tracks'].extend(response['items'])
            if response['next'] is None:
                break
            response = self.client.next(response)

        if len(playlist['tracks']) != playlist['total_tracks']:
            raise Exception('To Do')

        self.obj = playlist

    def to_generic(self):
        data = self.obj
        for ite, track in enumerate(data['tracks']):
            data['tracks'][ite] = GenericTrackObj(track['track']).__dict__

        self.generic_data = GenericPlaylistObj(data).__dict__
