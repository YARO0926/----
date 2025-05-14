name=input("학생 이름을 입력하세요 : ")

kor=int(input("국어 점수를 입력하세요 : "))

eng=int(input("영어 점수를 입력하세요 : "))
com=int(input("컴퓨터 점수를 입력하세요 : "))

ave=(kor+eng+com)/3

print("%s의 평균 점수는 %f점 입니다."%(name, ave))

print("%s의 평균 점수는 %d점 입니다."%(name, ave))
print("%s의 평균 점수는 %.2f점 입니다."%(name, ave))
