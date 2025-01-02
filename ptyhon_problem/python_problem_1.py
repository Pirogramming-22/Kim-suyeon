#8단계
def brGame(player_name, opponent_name):
    global num
    while True:
        inputCount = input("부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능) : ")
        try:
            numberCount = int(inputCount)
            if numberCount not in [1,2,3]:
                print("1,2,3 중 하나를 입력하세요")
            else:
                for i in range(numberCount):
                    num+=1
                    print("{0} : {1}".format(player_name,num))
                    if num == 31:
                        print("{0} win!".format(opponent_name)) 
                        exit()
                break
        except ValueError:
            print("정수를 입력하세요")


num = 0
while num < 31:
    brGame("playerA", "playerB")
    brGame("playerB","playerA")