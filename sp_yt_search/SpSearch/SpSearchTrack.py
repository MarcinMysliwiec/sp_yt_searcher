from .Sp import Sp
from .objects.GenericTrackObj import GenericTrackObj


class SpSearchTrack(Sp):
    def __init__(self, track_id):
        self.track_id = track_id
        super(SpSearchTrack, self).__init__()

    def search(self):
        self.obj = self.client.track(self.track_id)

    def to_generic(self):
        self.generic_data = GenericTrackObj(self.obj).__dict__
