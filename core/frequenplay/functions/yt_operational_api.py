import urllib.request, json

YTLEMNOSLIFEINSTANCE = "https://yt.lemnoslife.com/"
LOCALHOST = "http://localhost/YouTube-operational-API/"

class ytOperationalApi:
    def __init__(self, api_key="noKey", instance=LOCALHOST):
        self._api_key = api_key
        self._instance = instance

    def generate_timestamp_intensities(self, video_id: str) -> list[dict]:
        """
        Returns a list of 100 dictionary entries each containing 2 keys:
        startMillis is the timestamp, in miliseconds, when a replay occurred.
        intensityScoreNormalized is the normalized score of all replays.
        """
        with urllib.request.urlopen(self._instance + "/videos?part=mostReplayed&id=" + video_id) as request:
            data = json.load(request)
            return data["items"][0]["mostReplayed"]['markers']

    def get_api_key(self):
        return self._api
    
    def get_instance(self):
        return self._instance