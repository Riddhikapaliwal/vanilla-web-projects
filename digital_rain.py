import random
import time

character="0123456789"

while(True):
    line=""
    for _ in range(170):
        line += random.choice(character) if random.random()<0.15 else " "
    print(line)
    time.sleep(0.2)