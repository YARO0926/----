inFp, outFp = None, None

source = input("소스 파일명 입력하세요: ") 
tartget= input("타깃 파일명 입력하세요: ") 

inFp = open(source, "r", encoding= 'UTF8')
outFp = open(tartget, "w", encoding= 'UTF8')

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("---%s파일 %s파일로 복사되었음---" %(source, tartget))