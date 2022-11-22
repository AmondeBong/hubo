class Bank:
    def __init__(self):
        self.balance = 0

    def isEmptyMoney(self, money: int) -> bool:
        if (money > self.balance):
            return True
        else:
            return False

    def deposit(self, money: int):
        print("입금 전 금액: ", end=" ")
        print(self.balance)
        print("입금 금액: ", end=" ")
        print(money)
        self.balance += money
        self.check()

    def withdraw(self, money: int):
        if (self.isEmptyMoney(money)):
            print(" 인출할 돈이 없습니다.")
        else:
            print("출금 전 금액: ", end=" ")
            print(self.balance)
            print("출금 금액: ", end=" ")
            print(money)
            self.balance -= money
            self.check()

    def check(self):
        print("현재 통장 잔액 : ", end=" ")
        print(self.balance)


if __name__ == "__main__":
    play = True
    bank = Bank()

    while (play):
        select = input(
            " 은행 업무를 선택하시오: (d): deposit, (w):withdraw, (c):check , (e):exit  ---> ")

        if (select == 'd' or select == 'D' or select == 'ㅇ'):
            money = int(input("입금 금액을 입력하시오: "))
            bank.deposit(money)

        elif (select == 'w' or select == 'W' or select == 'ㅈ'):
            money = int(input("출금 금액을 입력하시오: "))
            bank.withdraw(money)

        elif (select == 'c' or select == 'C' or select == 'ㅊ'):
            bank.check()

        elif (select == 'e' or select == 'E' or select == 'ㄷ'):
            play = False
        else:
            print("다시 입력하시오.")
