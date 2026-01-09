# Process and reformat text lines from file

with open("King Lear.txt", "r") as f:
    list_content = f.readlines()

for index in range(len(list_content)):
    if list_content[index].isupper():
        list_content[index] = "\n" + list_content[index] + "\n"
    else:
        list_content[index] = "\t" + list_content[index]

with open("King Lear2.txt", "w") as f2:
    for element in list_content:
        f2.write(element)
