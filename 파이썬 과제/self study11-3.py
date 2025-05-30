outFp = None
outStr = ""

fileName= input("파일 이름 입력: ")

outFp = open("C:\\cjwony0926\\대학관련\\파이썬 과제\\fileTest\\%s.txt" %fileName, "w", encoding= 'UTF8')

while True:
    outStr = input("내용을 입력: ")
    if outStr != "":
        outFp.writelines(outStr + "\n")
    else:
        break

outFp.close
print("--- 정상적으로 파일에 씀 ---")