#append
#The append() method adds an item to the end of an existing list.
nums = [1, 2, 3, 5]
print('old nums is :', nums) # old nums is : [1, 2, 3, 5]
nums.append(4)
print('Updated nums is :', nums) # Updated nums is : [1, 2, 3, 5, 4]

#insert
#The insert() method lets you insert a new item at a certain index in the list
names = ['1 Marmik', "2 Jignesh", "4 Monik", '5 Rahul']
print(names) # ['1 Marmik', '2 Jignesh', '4 Monik', '5 Rahul']
names.insert(2, "3 Hiren")
print(names) # ['1 Marmik', '2 Jignesh', '3 Hiren', '4 Monik', '5 Rahul']

#index
# The index() method is find the first occurrence of an item in the list and returns its index
n = ['a', 'b', 'c', 'd', 'e']
print(n.index('b')) # 1
print(n.index('e')) # 4

#count
#The count() method returns how many times an item occurs in a list:
x = [1, 3, 4, 5, 5, 6, 4, 5, 5]
print(x.count(5)) # 4
print(x.count(3)) # 1

#remove : The remove() method removes an item from the list.
x = ["Mengo", "Watermelon", "Coconut"]
print(x) # ['Mengo', 'Watermelon', 'Coconut']
x.remove('Coconut')
print(x) # ['Mengo', 'Watermelon']
