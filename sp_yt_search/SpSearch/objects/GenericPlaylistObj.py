OBJECT_TYPE = 'playlist'


class GenericPlaylistObj:
    def __init__(self, album):
        self.type = OBJECT_TYPE
        self.id = album['id']
        self.uri = album['uri']
        self.name = album['name']
        self.snapshot_id = album['snapshot_id']
        self.total_tracks = album['total_tracks']
        self.tracks = album['tracks']
