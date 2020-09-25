OBJECT_TYPE = 'artist'


class GenericArtistObj:
    def __init__(self, artist):
        self.type = OBJECT_TYPE
        self.id = artist['id']
        self.uri = artist['uri']
        self.name = artist['name']
        self.albums = artist['albums']
