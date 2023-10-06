import random

class Player():

    def __init__(self, money):
        self.money = money
        self.hand = []
        self.money_burnt = 0

    def bet(self):

        betted = "not a digit"

        while (betted.isdigit() == False) or (int(betted) > self.money):
            betted = input('How much are you betting, which you can afford of course? ')

        self.money_burnt = int(betted)
        self.money = self.money - self.money_burnt
        return self.money_burnt

    def hit_or_stick(self):
        pass

    def hand_total(self):

        total_of_cards = []
        has_ace = False

        for card_object in self.hand:
            total_of_cards.append(card_object.value)

        the_hand_value = sum(total_of_cards)

        if the_hand_value > 21:
            for card_object in self.hand:
                if card_object.face == "Ace":
                    the_hand_value = the_hand_value - 10
        else:
            pass

        return the_hand_value

    def black_jack(self):
        print("BLACK JACK!")
        self.money = self.money + self.money_burnt + (self.money_burnt * 1.5)
        amount_won = self.money_burnt + (self.money_burnt * 1.5)
        print(f"You won {amount_won}!")

    def doubled_down_won(self):
        self.money = self.money + (self.money_burnt * 4)
        money_won = self.money_burnt * 4
        print(f'You won {money_won} moneys by Doubling Down!')

    def wins_hand(self):
        print("You win!")
        self.money = self.money + (self.money_burnt * 2)
        money_won = self.money_burnt * 2
        print(f"You won {money_won} moneys!")

    def player_hand(self):
        print(self.hand)

    def clear_hand(self):
        self.hand = []

    def __str__(self):
        return f"The player has {self.money} moneys, currently."

class Card():

    def __init__(self, suit, face):
        self.suit = suit
        self.face = face
        self.value = values[face]

    def __str__(self):
        return self.face + " of " + self.suit

    def give_value(self):
        return self.value

class Deck():

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for face in faces:
                created_card = Card(suit, face)

                self.all_cards.append(created_card)

    def shuffle(self):

        random.shuffle(self.all_cards)

    def count_deck(self):
        return len(self.all_cards)

    def deal_card(self):
        return self.all_cards.pop()


class Dealer():

    def __init__(self):

        self.hand = []

    def house_hand_first(self):
        print("The dealer is showing ")
        print(self.hand[1])

    def house_hand_turn(self):
        print("The dealer's hand is ")
        print(self.hand)

    def hand_total(self):
        total_of_hand = []

        for card_object in self.hand:
            total_of_hand.append(card_object.value)

        the_hand_value = sum(total_of_hand)

        if the_hand_value > 21:
            for card_object in self.hand:
                if card_object.face == "Ace":
                    the_hand_value = the_hand_value - 10
        else:
            pass

        return the_hand_value

    def clear_hand(self):
        self.hand = []


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
faces = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

buyin = 'unknown'

while buyin.isdigit() == False:
    buyin = input('How much moneys are you putting on the table? ')

player_money = int(buyin)
gambler = Player(player_money)

gambling = True
# while gambling = True
while gambling == True:

    bust = False
    game_deck = Deck()
    game_deck.shuffle()

    the_dealer = Dealer()
    if gambler.money == 0:
        print("You're poor now, bye bye <3.")
        break

    print(gambler)
    amount_bet = gambler.bet()

    player_card_1 = game_deck.deal_card()
    dealer_card_1 = game_deck.deal_card()
    player_card_2 = game_deck.deal_card()
    dealer_card_2 = game_deck.deal_card()

    gambler.hand.append(player_card_1)
    gambler.hand.append(player_card_2)
    the_dealer.hand.append(dealer_card_1)
    the_dealer.hand.append(dealer_card_2)

    print("\nThe player's hand is:")
    for card_object in gambler.hand:
        print(card_object)
    print("\nThe dealer's hand is a face down card and:")
    print(dealer_card_2)

    if player_card_1.value + player_card_2.value == 21:
        gambler.black_jack()
    else:
        down_doubled = False
        decision = 'not_pickable'
        while gambler.hand_total() <= 21 and decision != 'S' and decision != 'DD':

            decision = 'not_pickable'
            while decision != ('H' or 'S'):
                decision = input('\nHit, Stay or Double Down (H/S/DD): ')

                if decision == 'H':
                    gambler.hand.append(game_deck.deal_card())
                    print("\nThe player's hand is:")
                    for card_object in gambler.hand:
                        print(card_object)
                    print(gambler.hand_total())
                    break
                if decision == 'S':
                    break

                if decision == 'DD':
                    down_doubled = True
                    gambler.money = gambler.money - gambler.money_burnt
                    gambler.hand.append(game_deck.deal_card())
                    print(f"\nYou Doubled Down by betting another {gambler.money_burnt} moneys!")
                    print("The player's hand is:")
                    for card_object in gambler.hand:
                        print(card_object)
                    print(gambler.hand_total())
                    break

            if gambler.hand_total() > 21:
                print("Bust!")
                bust = True
                break

        if bust == False:

            print("\nThe dealer's hand is: ")
            for card_object in the_dealer.hand:
                print(card_object)

            print(the_dealer.hand_total())

            if the_dealer.hand_total() == 21:
                print("The dealer has BLACKJACK!")

            while the_dealer.hand_total() < 17:

                the_dealer.hand.append(game_deck.deal_card())
                print("\nThe dealer's hand is: ")
                for card_object in the_dealer.hand:
                    print(card_object)
                print(the_dealer.hand_total())

                if the_dealer.hand_total() >= 17 and the_dealer.hand_total() < 22:
                    print("\nThe dealer must stay!")
                    print(the_dealer.hand_total())
                    break

                elif the_dealer.hand_total() > 21:
                    print("\nThe dealer BUST!")
                    print(the_dealer.hand_total())
                    break

            if the_dealer.hand_total() > gambler.hand_total() and the_dealer.hand_total() <= 21:

                print("\nThe dealer wins!")

            elif the_dealer.hand_total() == gambler.hand_total():
                print(f"\nPUSH! You get {gambler.money_burnt} moneys back.")
                gambler.money = gambler.money + gambler.money_burnt

            elif down_doubled == True and gambler.hand_total() <= 21 and gambler.hand_total() > the_dealer.hand_total():
                gambler.doubled_down_won()


            else:
                gambler.wins_hand()

    gambler.clear_hand()
    the_dealer.clear_hand()

    print(f"\nYou have {gambler.money} moneys!")
    answer = 'idk'
    while answer != 'Y' or 'N':
        answer = input('\nAnother hand? (Y/N) ')

        if answer == 'Y' or answer == 'N':
            break

    if answer == 'Y':
        gambling = True
    if answer == 'N':
        print("Cheers!")
        gambling = False