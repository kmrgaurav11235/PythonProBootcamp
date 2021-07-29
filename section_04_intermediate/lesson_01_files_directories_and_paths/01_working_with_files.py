file = open("01_my_file.txt")  # open file
contents = file.read()  # read file
print(contents)
file.close()  # close file

# Use 'with' keyword and you will not need to close the file
with open(file="01_my_file.txt") as text_file:
    contents = text_file.read()
    print(contents)
    # No need for file.close()

with open(file="01_my_file.txt", mode="a") as text_file:  # open file in append mode. Another is write mode: "w"
    text_file.write("\nNone have ever caught him yet, for Tom, he is the master,")
    text_file.write("\nHis songs are stronger songs, and his feet are faster.")

# If you try to open a file in write mode and it doesn't exists, the file will get created.

