import sys, os
sys.path.append(os.path.abspath("frequenplay"))

from frequenplay_game import frequenplayGame

if __name__ == "__main__":
    fg_test = frequenplayGame("https://www.youtube.com/watch?v=oL5XNGhelGI", "11/05/2023", "Troll")
    fg_test.print_time()