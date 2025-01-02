#1단계: 변수 num 선언
num = 0

#6단계
while num < 31:
    #3단계
    while True:
        #2단계: input()함수 이용
        inputCount = input("부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능) : ")
        try:
            numberCount = int(inputCount)
            if numberCount not in [1,2,3]:
                print("1,2,3 중 하나를 입력하세요")
            else:
                #4단계
                for i in range(numberCount):
                    num+=1
                    print("playerA : {0}".format(num))
                    if num == 31:
                        print("playerB win!")
                        exit()
                break
        except ValueError:
            print("정수를 입력하세요")

    #5단계
    while True:
        inputCount = input("부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능) : ")
        try:
            numberCount = int(inputCount)
            if numberCount not in [1,2,3]:
                print("1,2,3 중 하나를 입력하세요")
            else:
                for i in range(numberCount):
                    num+=1
                    print("playerB : {0}".format(num))
                    if num == 31:
                        print("playerA win!")
                        exit()
                break
        except ValueError:
            print("정수를 입력하세요")
