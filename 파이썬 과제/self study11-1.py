inFp = None
inStr = ""
num = 0

inFp = open("C:\\cjwony0926\\대학관련\\파이썬 과제\\fileTest\\text.txt", "r", encoding= 'UTF8')

while True:
    num += 1
    inStr = inFp.readline()
    if inStr == "":
        break
    print("%d: %s" %(num, inStr), end = "")


inFp.close()