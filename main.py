import sys, os
sys.path.append(os.path.abspath("frequenplay"))

import frequenplay_game as fg

if __name__ == "__main__":
    fg_test = fg.frequenplayGameMC("https://www.youtube.com/watch?v=oL5XNGhelGI", "11/05/2023", "Troll")
    fg_test.generate_random_answer_bank(5)
    fg_test._print_answer_bank()