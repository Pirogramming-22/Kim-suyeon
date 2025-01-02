#1단계: 변수 num 선언
num = 0

#2단계: input()함수 이용
inputCount = input("부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능) : ")

#3단계
while True:
    try:
        numberCount = int(inputCount)
        if numberCount not in [1,2,3]:
            print("1,2,3 중 하나를 입력하세요")
    except ValueError:
        print("정수를 입력하세요")
    break
