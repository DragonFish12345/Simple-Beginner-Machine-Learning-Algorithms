import random

f = open('plusonedata.csv', 'a')

for i in range(0, 1000):
    num = random.randint(0, 1000000000000)
    f.write(f'{num};{num+1}\n')
