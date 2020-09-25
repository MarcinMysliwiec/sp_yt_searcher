from .SpSearchAlbum import SpSearchAlbum
from .SpSearchArtist import SpSearchArtist
from .SpSearchPlaylist import SpSearchPlaylist
from .SpSearchTrack import SpSearchTrack

TRACK_STRATEGY_NAME = 'track'
PLAYLIST_STRATEGY_NAME = 'playlist'
ALBUM_STRATEGY_NAME = 'album'
ARTIST_STRATEGY_NAME = 'artist'


def SpStrategy(uri):
    strategy_name = list(uri.split(":"))[1]
    resource_id = list(uri.split(":"))[2]

    if strategy_name == TRACK_STRATEGY_NAME:
        return SpSearchTrack(resource_id)
    if strategy_name == PLAYLIST_STRATEGY_NAME:
        return SpSearchPlaylist(resource_id)
    if strategy_name == ALBUM_STRATEGY_NAME:
        return SpSearchAlbum(resource_id)
    if strategy_name == ARTIST_STRATEGY_NAME:
        return SpSearchArtist(resource_id)

    raise Exception('To Do')