inFp = None
inLinst, inStr = [], ""
num = 0


inFp = open("C:\\cjwony0926\\대학관련\\파이썬 과제\\fileTest\\text.txt", "r", encoding= 'UTF8')

inList= inFp.readlines()

for inStr in inList:
    num += 1
    print("%d: %s" %(num, inStr), end = "")

inFp.close()