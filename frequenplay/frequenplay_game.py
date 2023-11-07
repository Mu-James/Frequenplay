from extract import extract_youtube_video_id_from_url
from yt_operational_api import ytOperationalApi
from search import mostReplayedSearch

class frequenplayGame:
    def __init__(self, yt_video_url: str, date_created: str, name: str):
        self.yt_video_url = yt_video_url
        self.yt_video_id = extract_youtube_video_id_from_url(yt_video_url)
        self.date_created = date_created
        self.name = name

        self._replay_timestamps = ytOperationalApi().generate_timestamp_intensities(self.yt_video_id)
        self._most_replayed = mostReplayedSearch(self._replay_timestamps)

    def print_time(self):
        print(self._most_replayed)

if __name__ == "__main__":
    fg = frequenplayGame("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "11/05/2023", "Troll")
    fg.print_time()