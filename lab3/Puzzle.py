c=int(input('Number of heads: '))
r= int(input('Number of legs: ')) 
def Solve(numheads, numlegs):
    rabbits = (numlegs/2) - numheads
    chicken = numheads - rabbits
    print(f'There is {int(rabbits)} rabits and {int(chicken)} chickens')
Solve(c,r)