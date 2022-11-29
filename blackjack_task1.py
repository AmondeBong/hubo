import random


### 1. FACES and SUITS list 작성



class Card:
  """A card has a face and suit."""

  def __init__(self, face, suit):
    ### 2.  assert를 사용해서 face와 suit가 FACES와 SUITS에서만 뽑히도록 하고, face suit attribute 작성

  def __str__(self):
    article = "a "
    if self.face in [8, "Ace"]: 
      article = "an "
    ### 3.  an 8 of diamond, a Queen of spade 같은 꼴의 str 리턴

  def value(self):
    """Returns the face value of the card."""
    ### 4. J Q K는 10, A는 11 리턴



class Deck(object):
  """A deck of cards."""
  def __init__(self):
    """Create a deck of 52 cards and shuffle them."""
    ### 5. 52개의 카드를 만들고 random module을 사용, 섞으시오


  def draw(self):
    """Draw the top card from the deck."""
    return self.cards.pop()




def hand_value(hand):
  """Computes the value of a hand of cards."""
  ### 6. 각 hand가 input으로 들어왔을 때 전체 value의 합을 계산하시오






def ask_yesno(prompt):
  """
  Display the text prompt and let the user enter a string.
  If the user enters "y", the function returns "True",
  and if the user enters "n", the function returns "False"
  If the user enters anything else, the function prints "I beg your pardon!",
  and asks again, repeating this until the user has entered a correct string.
  """
  
  ### 7. prompt를 보여주고, user가 y나 n를 입력하게 함, y이면 True를 반환, n이면 False를 반환 둘 다 아니면 "I beg your pardon"





      
def blackjack():
  """Play one round of Blackjack.
  Returns 1 if player wins, -1 if dealer wins, and 0 for a tie."""
  

  ##################### 블랙잭 한번의 라운드, player가 이기면 1을 반환, 딜러가 이기면 -1, 비기면 0 반환


  deck = Deck()
  dealer_cards = []
  player_cards = []



  ###### 8.  initial two cards (처음 두장 받기)  
  #  dealer_cards 및 player_cards에 appned를 하면서 받은 카드에 따라서 아래와 같이 프린트가 되야함 
  #  You are dealt a 9 of Hearts.
  #  Dealer is dealt a hidden card.
  #  You are dealt a 2 of Spades.
  #  Dealer is dealt a King of Diamonds. 
  #  your total is 11











  ### 9. player's turn to draw cards
  # 플레이어의 total value가 21보다 작으면 "Would you like another card? (y/n) "을 물어보고, n이면 딜러 턴으로 넘어가고 
  # y이면 한장 더 주기
  # 플레이어가 어떤 카드를 받았는지와, total value를 print해줘야함 
  # "You are dealt a 2 of clubs."
  # "your total is 13"
  # 플레이어의 카드값이 21보다 크면 "You went over 21! You lost!"를 프린트하고 경기 끝  
  # 플레이어가 카드를 더이상 받지 않으면, 딜러의 차례로 넘어감   






  ###10. dealers'turn to draw cards
  # 딜러의 hidden card를 보여줌 
  # "The dealer's hidden card was 8 of spades"
  # dealer의 total value가 17보다 작으면 카드를 더뽑고, total value를 프린트해줘야 함 
  # "Dealer is dealt a 2 of Diamonds."
  # "The dealer's total is 20"
  #  17보다 크면 아래로 넘어감




  ### 11. player의 total 점수와, dealer의 total 점수를 프린트 해주고 
  # "your total is 13"
  # "The dealer's total is 20"
  # 플레이어와 딜러의 점수에 따라, 
  # "You win!" 프린트하고 1 반환 혹은
  # "The dealer went over 21! You win!" 프린트하고 1 반환 혹은
  # "You lost" 프린트하고 -1 반환 혹은
  # "You have a tie" 를 프린트하고, 0 반환
  













######################################################################################################
def game_loop():
  print("Welcome to Blackjack 101!")   
  while True:
    print
    blackjack()    
    if not ask_yesno("\nPlay another round? (y/n) "):
      break    

game_loop()
