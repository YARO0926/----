base=int(input("입력 진수 결정"))
num=input("값 입력")

num=int(num, base)

hex=hex(num)
oct=oct(num)
bin=bin(num)

print("16진수==>"+hex)
print("8진수==>"+oct)
print("2진수==>"+bin)
print("2진수==>"+str(num))