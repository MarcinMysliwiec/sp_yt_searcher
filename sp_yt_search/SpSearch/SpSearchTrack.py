from .Sp import Sp
from .objects.GenericObj import GenericTrackObj


class SpSearchTrack(Sp):
    def __init__(self, track_id):
        self.track_id = track_id
        super(SpSearchTrack, self).__init__()

    def search(self):
        return self.client.track(self.track_id)

    def to_generic(self):
        return GenericTrackObj(self.data).__dict__
