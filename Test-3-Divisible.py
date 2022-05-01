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