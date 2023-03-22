# file = open("my_file.txt")
# or:
with open("my_file.txt", "a") as file:  # "a" stands for "append"
    file.write("\nNew text.")

with open("my_file.txt", "r") as file:
    contents = file.read()
    print(contents)

with open("new_file.txt", "w") as file:  # If write mode is used, the file is created if it does not exist.
    file.write("Some text.")

# Let's free up resources. Do not use with "with" keyword.
# file.close()
