def isPrimeNumber_v1 (n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
        else:
            return True
        
def isPrimeNumber_v2 (n):
    return 0 not in map(lambda i: n % i, range(2, int(n**0.5+1)))

def txtToBool(str):
    return True if (str[0] == "T") else False

def cmpTwoFiles(fileA, fileB):
    listA = fileA.readlines()
    listB = fileB.readlines()
    listResult = []
    for i in range(len(listA)):
        # if isPrimeNumber_v1(int(listA[i])) == txtToBool(listB[i]):
        if isPrimeNumber_v2(int(listA[i])) == txtToBool(listB[i]):
            listResult.append("pass\n")
        else:
            listResult.append("fail " + str(listB[i]))
            
    return listResult

fInput = open("input.txt", "r")
fResult = open("result.txt", "w")
fOutput = open("output.txt", "r")

listResult = cmpTwoFiles(fInput, fOutput)

for result in listResult:
    fResult.write(result);
    
fInput.close()
fResult.close()
fOutput.close()