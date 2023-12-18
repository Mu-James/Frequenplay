from extract import extract_youtube_video_id_from_url
from yt_operational_api import ytOperationalApi
from search import mostReplayedSearch

from collections import defaultdict

class frequenplayGame:
    def __init__(self, yt_video_url: str, date_created: str, name: str):
        self.yt_video_url = yt_video_url
        self.yt_video_id = extract_youtube_video_id_from_url(yt_video_url)
        self.date_created = date_created
        self.name = name

        self._replay_timestamps = ytOperationalApi().generate_timestamp_intensities(self.yt_video_id)
        self._most_replayed = mostReplayedSearch(self._replay_timestamps)

    def _print_most_replayed(self):
        print(self._most_replayed)

    def _print_replay_timestamps(self):
        print(self._replay_timestamps)

class frequenplayGameMC(frequenplayGame):
    def __init__(self, yt_video_str: str, date_created: str, name: str):
        super().__init__(yt_video_str, date_created, name)

        self.possible_multiple_answers = False
        if (len(self._most_replayed) < 1):
            self.possible_multiple_answers = True
        self.has_multiple_answers = False
        self.answer_bank = defaultdict(None)