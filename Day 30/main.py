# try: something that might cause an exception
# except: do this if there was an exception
# else: do this there were no exception
# finally: do this no matter what happens

# FileNotFound
try:
    file = open("a_file.txt")
    a = [1, 2, 3, 4]
    # print(a[8])
except FileNotFoundError:
    open("a_file.txt", "w")
except IndexError as index:
    print(f"Error: {index}")
else:
    print("I only run when the try statement didn't raise an exception")
finally:
    print("I am persistent and can run no matter what happened")

#----------------------EXERCISE I---------------------------
fruits = ["Apple", "Pear", "Orange"]

def make_pie(idx):
    try:
        fruit = fruits[idx]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")

make_pie(4)

#----------------------EXERCISE I---------------------------
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass


print(f"total likes: {total_likes}")
