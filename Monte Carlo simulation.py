#-----Explanation-----

#Q. You are exploring a new city, which is divided into perfect blocks, by taking a walk outside.
#   If the distance between the starting point and your current position is greater than 4 blocks, you will need a transport to get back.
#   You are allowed to move north, south, east, or west. Backward movement is also permitted.
#   What is the longest random walk you can take, so that you will not require a transport to get back?

#The program applies the Monte Carlo method using random fn to solve this.
#Considering the maximum number of blocks to be 50.

import random

def random_walk(n):
    #returns coordinates after 'n' blocks of random walks
    x,y = 0,0
    for i in range(n):
        (dx,dy) = random.choice([(0,1), (0,-1), (1,0), (-1,0)])
        x += dx
        y+= dy
    return x,y

#Considering 10000 walks to get an accurate result
number_of_walks = 10000

for walk_length in range(1,51):
    #Checks for the requirement of a transport
    no_transport = 0
    for i in range(number_of_walks):
        (x,y) = random_walk(walk_length)
        distance = abs(x) + abs(y)
        if distance <=4:
            no_transport += 1
    #to find the % of no requirement for transport
    no_transport_percentage = float(no_transport) / number_of_walks
    #to print all the individual cases
    print("Walk size = ",walk_length,
          "/ % of no requirement for transport = ",100*no_transport_percentage)
    if 100*no_transport_percentage >= 50.00:
        #to get the block distance for the largest walk
        largest_walk = walk_length
        #to get % of no requirement for transport for the largest walk
        largest_percentage = 100*no_transport_percentage

#to print the desired case
print("\nLargest walk with higher than 50% chance of no transport needed is",largest_walk,"blocks",
      "with a percentage of",largest_percentage,"%.")
