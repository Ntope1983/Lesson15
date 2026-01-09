# Generate random numbers and save them to a text file
with open("test2.txt", "r") as f:
    lines=f.readlines()
    print(lines)
    newlines=[line.strip() for line in lines]
print(newlines)
