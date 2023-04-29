from collections import Counter
sample = [2, 3, 6]
y = lambda sample: sample [0] * sample [1] * sample [2]
print(y(sample))


sample1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
def sort_items(sample1):
    return sample1[1]
sample1.sort(key= sort_items)
print(sample1)

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
d = Counter(d1) + Counter(d2)
print(d)

number = int(input("Type a number: "))
for n in range(number):
    n = n + 1
    dictionary = {(n, n ** 2)}
    print(dictionary)

list = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
list.sort(reverse=True)
for n in list:
    print(n[1])

set = {0, 1, 2, 3, 4}
for n2 in set:
    print(n2)
choice = input("what would you like to do ?")
if choice == "add":
    add = input("who do you want to add: ")
    set.add(add)
    print(set)
elif choice == "remove":
    remove = input("who do you want to remove: ")
    set.remove(remove)
    print(set)
else: print ("error 404")


