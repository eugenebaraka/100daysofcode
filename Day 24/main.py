file = open("testfile.txt") # when python opens up this file,
# it takes up computer resources. Therefore, it is very important to close it
# to make sure you free up the space for great performance
contents = file.read()
# print(contents)
file.close()


# A different way of opening the file so that it automatically closes
with open("testfile.txt") as file:
    contents2 = file.read()
    print(contents2[-1])

# with open("new_file.txt", mode="a") as file: #if you do not specify mode, it is "read only" by default
#     file.write("I am also learning computer theory")
