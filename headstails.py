import random

numberOfFlips = 0
heads = 0
tails = 0
streakcount = 0 

#if numberOfFlips < 100:
for flips in range(10000):
    numberOfFlips += 1
    #print('***' + str(numberOfFlips) + '***')
    
    result = random.randint(0, 1)
    if result == 0:
        heads += 1
        print('H', end = ' ')
        tails = 0
        if heads == 6:
            streakcount += 1
            print('Streak hit 6!')
            heads = 0
            tails = 0
        
        #print(heads)
    if result == 1:
        tails += 1
        print('T', end = ' ')
        if tails == 6:
            streakcount += 1 
            print('Streak hit 6!')
            heads = 0
            tails = 0
        heads = 0
        #print(tails)

print(f'Game Over, there were {streakcount} streaks of 6 or more')
print('Chance in a streak %s%%' % (streakcount / 10000))           
        
        