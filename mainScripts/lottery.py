import random as rd

poll = list()

for i in range(1,61):
    poll.append(i)

prize1 = [9,56,27,25,32,5]

o = 0
game = [0,0,0,0,0,0]
while sorted(game) != sorted(prize1):
    game = rd.sample(poll,6)
    print(game)
    o+=1

print('\n',o,'\n')

