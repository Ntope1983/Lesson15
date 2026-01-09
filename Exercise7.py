# Merge contents of two files into a third file
def merge(filename1,filename2,filename):
    with open(filename,"a") as f:
        with open(filename1,"r") as f1:
            f.write(f1.read())
        with open(filename2,"r") as f2:
            f.write(f2.read())

merge("test2.txt","overwrite.txt","filename.txt")