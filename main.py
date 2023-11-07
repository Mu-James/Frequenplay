import sys, os
sys.path.append(os.path.abspath("frequenplay"))

print(sys.path)
from frequenplay_game import frequenplayGame

if __name__ == "__main__":
    fg1 = frequenplayGame("https://www.youtube.com/watch?v=oL5XNGhelGI", "11/05/2023", "Troll")
    fg1.print_time()