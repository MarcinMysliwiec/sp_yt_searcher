OBJECT_TYPE = 'album'


class GenericAlbumObj:
    def __init__(self, album):
        self.type = OBJECT_TYPE
        self.id = album['id']
        self.uri = album['uri']
        self.name = album['name']
        self.label = album['label']
        self.release_date = album['release_date']
        self.total_tracks = album['total_tracks']
        self.tracks = album['tracks']
