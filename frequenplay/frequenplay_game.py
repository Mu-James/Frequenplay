from extract import extract_youtube_video_id_from_url
from yt_operational_api import ytOperationalApi
from frequenplay.sort_timestamps import sortTimestamps

import random as r

class FrequenplayGameError(Exception):
    def __init__(self, message):
        super().__init__(message)

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
        self.num_total_timestamp_entries = self.num_mr_entries + self.num_o_entries

    def _print_most_replayed(self):
        print(self._most_replayed_timestamps)

    def _print_replay_timestamps(self):
        print(self._replay_timestamps)

class frequenplayGameMC(frequenplayGame):
    def __init__(self, yt_video_str: str, date_created: str, name: str):
        super().__init__(yt_video_str, date_created, name)

        self.has_multiple_answers = False
        if self.num_mr_entries < 1:
            self.has_multiple_answers = True
        self.uses_multiple_answers = False
        self.answer_bank = {}

    def _print_answer_bank(self):
        print(self.answer_bank)

    def enable_multiple_answers(self):
        if self.has_multiple_answers == True: 
            if self.uses_multiple_answers == False:
                self.uses_multiple_answers = True
            else:
                raise FrequenplayGameError("current instance has multiple answers enabled")
        else:
            raise FrequenplayGameError("current instance does not contain multiple answers")
        
    def disable_multiple_answers(self):
        if self.has_multiple_answers == True:
            if self.uses_multiple_answers == True:
                self.uses_multiple_answers = False
            else:
                raise FrequenplayGameError("current instance has multiple answers disabled")
        else:
            raise FrequenplayGameError("current instance does not contain multiple answers")

    def generate_random_answer_bank(self, num_choices: int):
        if (self.uses_multiple_answers == False and num_choices <=  self.num_total_timestamp_entries):
            self.answer_bank[self._most_replayed_timestamps[0]] = True
            for i in range(num_choices):
                choice = r.choice(self._other_timestamps)
                self.answer_bank[choice] = False
        elif (self.uses_multiple_answers == True and num_choices <=  self.num_total_timestamp_entries):
            num_correct_answers = r.randrange(self.num_mr_entries)
            for i in range(num_correct_answers):
                choice = r.choice(self._most_replayed_timestamps)
                self.answer_bank[choice] = True
            for i in range(num_choices - num_correct_answers):
                choice = r.choice(self._other_timestamps)
                self.answer_bank[choice] = False
        else:
            raise FrequenplayGameError("generate_random_answer_bank did not work correctly")           
            
