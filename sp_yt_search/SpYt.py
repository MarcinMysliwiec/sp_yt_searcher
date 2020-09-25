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

    def HasSpInstance(func):
        def inner(self):
            if self.sp_instance is None:
                raise Exception('To Do')
            func(self)

        return inner

    @HasSpInstance
    def get_sp_data(self):
        return self.sp_instance.generic_data
