OBJECT_TYPE = 'track'


class GenericTrackObj:
    def __init__(self, track):
        self.type = OBJECT_TYPE
        self.id = track['id']
        self.uri = track['uri']
        self.name = track['name']
        self.duration_ms = track['duration_ms']
        self.custom = self.parse_custom(track)

    def parse_custom(self, track):
        custom = dict();
        custom['duration'] = int(track['duration_ms'] / 1000)
        custom['full_name'] = ', '.join(
            [str(elem['name']) for elem in track['artists']]) + f" - {track['name']}"
        custom['is_remix'] = 'remix' in track['name'].lower()
        custom['is_instrumental'] = 'instrumental' in track['name'].lower()
        custom['is_live'] = 'live' in track['name'].lower()
        custom['is_official'] = not custom['is_remix'] and not custom['is_instrumental']
        return custom
