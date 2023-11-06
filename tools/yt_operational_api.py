import urllib.request, json

YTLEMNOSLIFEINSTANCE = "https://yt.lemnoslife.com/"

class ytOperationalApi:
    def __init__(self, api_key="noKey", instance=YTLEMNOSLIFEINSTANCE):
        self._api_key = api_key
        self._instance = instance

    def generate_most_replayed(self, video_id: str, instance: str) -> list[dict]:
        """
        Returns a list of 100 dictionary entries each containing 2 keys:
        startMillis is the timestamp, in miliseconds, when a replay occurred.
        intensityScoreNormalized is the normalized score of all replays.
        """
        with urllib.request.urlopen(instance + "/videos?part=mostReplayed&id=" + video_id) as request:
            data = json.load(request)
            return data["items"][0]["mostReplayed"]['markers']

    def get_api_key(self):
        return self._api
    
    def get_instance(self):
        return self._instance
    
if __name__ == "__main__":
    ytOA = ytOperationalApi()
    print(ytOA.generate_most_replayed("dQw4w9WgXcQ", YTLEMNOSLIFEINSTANCE))