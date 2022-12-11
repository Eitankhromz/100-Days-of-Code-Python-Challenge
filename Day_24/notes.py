#Open a file, reads it content, and close file
with open(r"..\..\Desktop\my_file.txt") as file:
    contents = file.read()
    print(contents)


