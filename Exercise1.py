# Generate random numbers and save them to a text file

import random
list_numbers=[random.randint(0,100) for number in range(1500)]
with open("numbers.txt","w") as f:
    for number in list_numbers:
        f.write(str(number)+"\n")