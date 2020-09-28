from .SpSearch.SpSettings import SpSettings
from .SpSearch.SpStrategy import SpStrategy


class SpYt:
    def __init__(self):
        self.uri = ''
        self.sp_instance = None

    def set_credentials(self, sp_client_id, sp_client_secret):
        SpSettings().SPOTIPY_CLIENT_ID = sp_client_id
        SpSettings().SPOTIPY_CLIENT_SECRET = sp_client_secret

    def sp_search(self, uri):
        self.uri = uri
        self.sp_instance = SpStrategy(uri)
        return self.sp_instance.to_generic()

