answer=0

type=int(input("1.입력한 수식 계산  2.두 수 사이의 합계"))
if type==1:
    expression=input("수식을 입력하세요")
    print(eval(expression))

elif type==2:
    num1=int(input('첫번째 숫자를 입력하세요'))
    num2=int(input('두번째 숫자를 입력하세요'))

    for i in range(num1, num2+1):
        
        answer=answer+i
    print(f"{num1}+....+{num2}는 {answer}입니다")

else:
    print("1또는 2를 입력하여주세요")