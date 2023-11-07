import sys, os
path = os.path.abspath("frequenplay")
sys.path.append(path)

print(sys.path)
from frequenplay_game import frequenplayGame

if __name__ == "__main__":
    fg1 = frequenplayGame("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "11/05/2023", "Troll")
    fg1.print_time()