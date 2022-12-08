import random


# 1. FACES and SUITS list 작성
Faces = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
Suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']


class Card:
    """A card has a face and suit."""

    def __init__(self, face, suit):
        # 2.  assert를 사용해서 face와 suit가 FACES와 SUITS에서만 뽑히도록 하고, face suit attribute 작성

        assert face in Faces, 'Faces 안에서만 뽑히도록 하시오'
        assert suit in Suits, 'Suits 안에서만 뽑히도록 하시오'
        self.face = face
        self.suit = suit

    def __str__(self):
        article = "a "
        if self.face in [8, "Ace"]:
            article = "an "
        # 3.  an 8 of diamond, a Queen of spade 같은 꼴의 str 리턴
        return (article + str(self.face) + ' of ' + self.suit)

    def value(self) -> int:
        """Returns the face value of the card."""
        # 4. J Q K는 10, A는 11 리턴
        if (self.face == 'Jack' or self.face == 'Queen' or self.face == 'King'):
            return 10
        elif (self.face == 'Ace'):
            return 11
        else:
            return self.face


class Deck(object):
    """A deck of cards."""

    def __init__(self):
        """Create a deck of 52 cards and shuffle them."""
        # 5. 52개의 카드를 만들고 random module을 사용, 섞으시오
        self.cards = []
        for suit in Suits:
            for face in Faces:
                self.cards.append(Card(face, suit))
        random.shuffle(self.cards)

    def draw(self):
        """Draw the top card from the deck."""
        return self.cards.pop()


def hand_value(hand: list) -> int:
    """Computes the value of a hand of cards."""
    # 6. 각 hand가 input으로 들어왔을 때 전체 value의 합을 계산하시오
    sum = 0
    for i in range(len(hand)):
        card = hand[i]
        sum += card.value()
    return sum


def ask_yesno() -> bool:
    """
    Display the text prompt and let the user enter a string.
    If the user enters "y", the function returns "True",
    and if the user enters "n", the function returns "False"
    If the user enters anything else, the function prints "I beg your pardon!",
    and asks again, repeating this until the user has entered a correct string.
    """
    play = True
    # 7. prompt를 보여주고, user가 y나 n를 입력하게 함, y이면 True를 반환, n이면 False를 반환 둘 다 아니면 "I beg your pardon"
    while (play):
        print()
        select = str(input('Would you like another card? (y/n) ----> '))
        if (select == 'y' or select == 'Y'):
            play = False
            return True
        elif (select == 'n' or select == 'N'):
            play = False
            return False
        else:
            print()
            print('I beg your pardon')


def blackjack() -> int:
    """Play one round of Blackjack.
    Returns 1 if player wins, -1 if dealer wins, and 0 for a tie."""

    # 블랙잭 한번의 라운드, player가 이기면 1을 반환, 딜러가 이기면 -1, 비기면 0 반환

    deck = Deck()
    dealer_cards = []
    player_cards = []

    # 8.  initial two cards (처음 두장 받기)
    #  dealer_cards 및 player_cards에 appned를 하면서 받은 카드에 따라서 아래와 같이 프린트가 되야함
    #  You are dealt a 9 of Hearts.
    #  Dealer is dealt a hidden card.
    #  You are dealt a 2 of Spades.
    #  Dealer is dealt a King of Diamonds.
    #  your total is 11

    i = len(deck.cards)-1  # deck의 인덱스

    a = 0  # player_cards의 인덱스
    b = 0  # dealer_cards의 인덱스

    player_cards.append(deck.cards[i])
    print('You are dealt '+player_cards[a].__str__())

    deck.draw()
    i -= 1
    a += 1

    dealer_cards.append(deck.cards[i])
    print('Dealer is dealt a hidden_card')
    hidden_card = deck.cards[b]
    deck.draw()
    i -= 1
    b += 1

    player_cards.append(deck.cards[i])
    print('You are dealt '+player_cards[a].__str__())

    deck.draw()
    i -= 1
    a += 1

    dealer_cards.append(deck.cards[i])
    print('Dealer is dealt '+dealer_cards[b].__str__())
    deck.draw()
    i -= 1
    b += 1

    print('your total is '+str(hand_value(player_cards)))

    # 9. player's turn to draw cards
    # 플레이어의 total value가 21보다 작으면 "Would you like another card? (y/n) "을 물어보고, n이면 딜러 턴으로 넘어가고
    # y이면 한장 더 주기
    # 플레이어가 어떤 카드를 받았는지와, total value를 print해줘야함
    # "You are dealt a 2 of clubs."
    # "your total is 13"
    # 플레이어의 카드값이 21보다 크면 "You went over 21! You lost!"를 프린트하고 경기 끝
    # 플레이어가 카드를 더이상 받지 않으면, 딜러의 차례로 넘어감

    if (hand_value(player_cards) < 21):
        if (ask_yesno()):
            player_cards.append(deck.cards[i])
            print('You are dealt '+player_cards[a].__str__())
            deck.draw()
            i -= 1
            a += 1

            print('your total is '+str(hand_value(player_cards)))
            print()
            if (hand_value(player_cards) >= 21):
                print('You went over 21! You lost')
                return -1

            # 10. dealers'turn to draw cards
            # 딜러의 hidden card를 보여줌
            # "The dealer's hidden card was 8 of spades"
            # dealer의 total value가 17보다 작으면 카드를 더뽑고, total value를 프린트해줘야 함
            # "Dealer is dealt a 2 of Diamonds."
            # "The dealer's total is 20"
            #  17보다 크면 아래로 넘어감
    print("The dealer's hidden card was "+str(hidden_card.__str__()))
    if (hand_value(dealer_cards) <= 17):
        dealer_cards.append(deck.cards[i])
        print('Dealer is dealt '+dealer_cards[b].__str__())
        deck.draw()
        i -= 1
        b += 1
        print("The dealer's total is " + str(hand_value(dealer_cards)))

        # 11. player의 total 점수와, dealer의 total 점수를 프린트 해주고
        # "your total is 13"
        # "The dealer's total is 20"
        # 플레이어와 딜러의 점수에 따라,
        # "You win!" 프린트하고 1 반환 혹은
        # "The dealer went over 21! You win!" 프린트하고 1 반환 혹은
        # "You lost" 프린트하고 -1 반환 혹은
        # "You have a tie" 를 프린트하고, 0 반환

    print()
    print('your total is '+str(hand_value(player_cards)))
    print("The dealer's total is " + str(hand_value(dealer_cards)))

    if (hand_value(dealer_cards) >= 21):
        print("The dealer went over 21! You win!")
        return 1
    elif (hand_value(player_cards) >= 21):
        print('You lost')
        return -1
    else:
        print('You have a tie')
        return 0

        ######################################################################################################


def ask_exit():
    play = True

    while (play):
        select = str(input('Would you like to play again ? (y/n) ----> '))
        if (select == 'y' or select == 'Y'):
            play = False
            return True
        elif (select == 'n' or select == 'N'):
            play = False
            return False
        else:
            print('Please enter y or n')


def game_loop():
    print("Welcome to Blackjack 101!")
    while True:
        print()
        blackjack()
        if not ask_exit():
            break


game_loop()
