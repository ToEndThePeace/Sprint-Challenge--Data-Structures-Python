import time
from binarytree import BSTNode

start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Return the list of duplicates in this data structure
duplicates = []

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# Testing if a set contains a value is much faster than a list :)
# and you don't need to iterate over its entirety!
# duplicates = set(names_1).intersection(names_2)

# doing with a binary tree because apparently i cheated
for i, x in enumerate(names_1):
    if i == 0:
        tree = BSTNode(x)
    else:
        tree.insert(x)

for y in names_2:
    if tree.contains(y):
        duplicates.append(y)



end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# 6s -> .006s :') I love python

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# USE A SET <3