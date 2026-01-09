# Copy the contents of one file into another
def copy_file(filename1, filename2):
    with open(filename1, "r") as f1:
        lines = f1.read()
    with open(filename2, "w") as f2:
        f2.write(lines)


copy_file("numbers.txt", "numbers2.txt")
