# Import the Scanner class

@staticmethod
def findAndContest( maps,  visited,  tempFraction,  row,  col,  x,  y) :
    # Map< String,Integer> fractions
    if (x < 0 or x >= row) :
        # make sure not not exceed the limit
        return
    if (y < 0 or y >= col) :
        # make sure not not exceed the limit
        return
    if (visited[x][y]) :
        # ignore it when already visited
        return
    visited[x][y] = True
    # set true when the maps is already visited
    if (maps[x][y]=="#") :
        # ignore #
        return
    if (not maps[x][y]==".") :
        # add fraction to the Set tempFraction
        tempFraction.append(maps[x][y])
    findAndContest(maps, visited, tempFraction, row, col, x, y + 1)
    # move direction right
    findAndContest(maps, visited, tempFraction, row, col, x, y - 1)
    # move direction left
    findAndContest(maps, visited, tempFraction, row, col, x + 1, y)
    # move direction up
    findAndContest(maps, visited, tempFraction, row, col, x - 1, y)
    # move direction down
    return



def main() :
    # input =  "Python-inputs"
    # File file = new File("test.in");
    # Scanner inputFile = new Scanner(file);
    testCase = input()
    listResultContest =  []
    listResultConquer =  []
    i = 1
    while (i <= testCase) :
        row = input()
        col = input()
        maps = [[None] * (col) for _ in range(row)]
        # map the input string to 2d array
        visited = [[False] * (col) for _ in range(row)]
        # array to store if the node is already visited
        tempFractions = set()
        # using set to store temp fraction
        fractions =  []
        # using tree map to store fraction by alpahbetical order
        j = 0
        while (j < row) :
            # init data 
            str = input()
            ch = list(str)
            k = 0
            while (k < len(ch)) :
                maps[j][k] = "".join(ch[k])
                visited[j][k] = False
                k += 1
            j += 1
        Conquer = 0
        j = 0
        while (j < row) :
            k = 0
            while (k < col) :
                tempFractions.clear()

                # reset temp fraction every region check
                findAndContest(maps, visited, tempFractions, row, col, j, k)

                tempITR = tempFractions.iterator()
                if (len(tempFractions) > 1) :
                    # if set fraction > 1 there's a contest
                    Conquer += 1
                else :
                    # if set = 1 then store value in set(tempfraction) to fraction
                    while (tempITR.hasNext()) :
                        frac = tempITR.next()
                        if (fractions.get(frac) != (None)) :
                            fractions[frac] = fractions.get(frac) + 1
                        elif(fractions.get(frac) == (None)) :
                            fractions[frac] = 1
                k += 1
            j += 1
        # result
        # System.out.println("Case "+i+":");
        # for(Map.Entry<String,Integer> entry : fractions.entrySet()) {
        #     String key = entry.getKey();
        #     Integer val = entry.getValue();
        #     System.out.println(key+" "+val);
        # }
        # System.out.println("contested "+Conquer);
        itemConquer = ""
        for entry in fractions.entrySet() :
            key = entry.getKey()
            val = entry.getValue()
            itemConquer += key + " " + str(val) + "_"
        listResultContest.append("contested " + str(Conquer))
        listResultConquer.append(itemConquer)
        i += 1
    i = 0
    while (i < testCase) :
        arrConquered = listResultConquer[i].split("_")
        print("Case " + str((i + 1)) + ":")
        for itemConquer in arrConquered :
            print(itemConquer)
        print(listResultContest[i])
        i += 1
    

main()
    