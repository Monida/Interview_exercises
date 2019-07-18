"""
Interview question: A NxN matrix is initialized randomly with some coins in 
row,col positions (row=rows, col=columns). A robot has to go from the start position
at (0,0) to the end position at (N-1,N-1) by only going to the right or down, trying
to collect as many coins as possible.
  
Category: Dynamic Programming

Description: This function takes a vector indicating the positions of the coins
and returns the maximum number of coins the robot could find.
"""

def find_coins(input_coins, N):
    max_coins=[[0 for col in range(N)] for row in range(N)]
    up=max_coins[0][0]
    left=max_coins[0][0]
    
    for row in range(N):
        for col in range(N):
            if row-1<0:
                up=0
            else:
                up=max_coins[row-1][col]
                
            if col-1<0:
                left=0
            else:
                left=max_coins[row][col-1]
            
            if up>=left:
                max_coins[row][col]=up
                
            else:
                max_coins[row][col]=left
            
            if [row,col] in input_coins:
                max_coins[row][col]+=1
    
    return max_coins[row][col]
                
#%% Test the function

N=5
input_coins=[[0,4],[1,0],[1,3],[2,2],[2,3],[2,4],[4,0]]

max_num_coins=find_coins(input_coins,N)    
    
    