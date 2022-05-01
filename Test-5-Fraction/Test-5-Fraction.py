def findAndContest(maps,visited,tempFraction,row, col,x, y):
    #Map< String,Integer> fractions
    if x < 0 or x >= row: # make sure not not exceed the limit
        return

    if(y < 0 or y >= col): # make sure not not exceed the limit
        return

    if(visited[x][y]): # ignore it when already visited
        return

    visited[x][y] = True # set true when the maps is already visited
    if maps[x][y] == "#": # ignore #
        return
    
    if maps[x][y] != ".": # add fraction to the Set tempFraction
        tempFraction.add(maps[x][y])

    findAndContest(maps,visited,tempFraction,row,col,x,y+1); # move direction right
    findAndContest(maps,visited,tempFraction,row,col,x,y-1); # move direction left
    findAndContest(maps,visited,tempFraction,row,col,x+1,y); # move direction up
    findAndContest(maps,visited,tempFraction,row,col,x-1,y); # move direction down
    return


arrayResult = []
testCase = int(input())

for i in range(testCase):
    ctr = 0
    a = int(input())    
    b = int(input())    
    k = int(input())
    
    for num in range(a, b + 1):
        if num % k == 0 : ctr = ctr + 1
    
    arrayResult.append(ctr)

for index in range(testCase):
    print("Case " + str(index + 1) + ": " + str(arrayResult[index]))