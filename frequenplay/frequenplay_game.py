from extract import extract_youtube_video_id_from_url
from yt_operational_api import ytOperationalApi
from frequenplay.sort_timestamps import sortTimestamps

from collections import defaultdict

class frequenplayGame:
    def __init__(self, yt_video_url: str, date_created: str, name: str):
        self.yt_video_url = yt_video_url
        self.yt_video_id = extract_youtube_video_id_from_url(yt_video_url)
        self.date_created = date_created
        self.name = name

        self._replay_timestamps = ytOperationalApi().generate_timestamp_intensities(self.yt_video_id)
        self._sorted_timestamps = sortTimestamps(self._replay_timestamps)

        self._most_replayed_timestamps = self._sorted_timestamps[0][0]
        self._other_timestamps = self._sorted_timestamps[1][0]

        self.num_mr_entries = self._sorted_timestamps[0][1]
        self.num_o_entries = self._sorted_timestamps[1][1]

    def _print_most_replayed(self):
        print(self._most_replayed_timestamps)

    def _print_replay_timestamps(self):
        print(self._replay_timestamps)

class frequenplayGameMC(frequenplayGame):
    def __init__(self, yt_video_str: str, date_created: str, name: str):
        super().__init__(yt_video_str, date_created, name)

        self.has_multiple_answers = False
        if (len(self._most_replayed) < 1):
            self.has_multiple_answers = True
        self.uses_multiple_answers = False
        self.answer_bank = defaultdict(None)