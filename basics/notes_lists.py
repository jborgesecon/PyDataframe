import dataValid as mu
import random as rd

#Lists
print('\nlists are mutable and very versitile objects:\n')
list1 = list()
print('the list will contain 10 items:')
for i in range(10):
    list1.append(rd.randint(0,100))

print('now the current list has the following elements:\n\n', list1)

list1[0] = 14
print(list1, 'new element added in position [0]')

del list1[8]
print(list1, 'item deleted at position [8]')

list1.pop()
print(list1, 'item deleted at last position')

list1.sort()
print(list1, 'list sorted') 

list1.sort(reverse=True)
print(list1, 'list reversed')

print(len(list1))

print('\nList correlation:\n')

list2 = list()

for i in range(12):
    list2.append(rd.randint(0,100))

list3 = list2
print(list2)
print(list3)
list2[-1] = 46
print('\n', list2)
print(list3, 'See that I only added 46 to the first list, but it showed up on both')
print('this happens because the lists are connected')

list4 = list2[:]
list4.pop()

print(list2)
print(list4, 'now the list4 is a copy of list2, and they are not connected')
