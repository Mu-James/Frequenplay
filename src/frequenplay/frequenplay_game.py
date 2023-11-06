from tools import extract as e
from tools import ytOperationalApi
from tools import search as s

class frequenplayGame:
    def __init__(self, yt_video_url: str, date_created: str, name: str):
        self.yt_video_url = yt_video_url
        self.yt_video_id = e.extract_youtube_video_id_from_url(yt_video_url)
        self.date_created = date_created
        self.name = name

        self._replay_timestamps = ytOperationalApi().generate_timestamp_intensities(self.yt_video_id)
        self._most_replayed = s.mostReplayedSearch(self._replay_timestamps)