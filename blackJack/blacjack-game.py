import os
import random
from blackjack_art import logo
#CapStone Project 1

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

is_running = True

def total_score(card_hand):
    card_sum = sum(card_hand)
    ace_count = card_hand.count(11)
    
    if card_sum == 21:
        card_sum = 0
    
    if ace_count > 0 and card_sum > 21:
        card_sum -= 10
        ace_count -= 1
    
    return card_sum


def deal_card(card_suitors, cards_to_deal):
    for i in range(cards_to_deal):
        random_index = random.randint(0, len(cards) - 1)            
        card_suitors.append(cards[random_index])
        
                
def compare(player_score, npc_score):
    
    if npc_score == player_score:
        print("draw🤔")
        
    elif player_score == 0:
        print("You win 😎, You have blackjack")
    
    elif npc_score == 0:
        print("You lose 😭, Opponent has blackjack")
    
    elif npc_score > 21:
        print("Opponent went Over. You win😎")
    
    elif player_score > 21:
        print("You went Over. You lose 😭")
    
    elif player_score > npc_score:
        print("You win😎")
        
    elif npc_score > player_score:
        print("You lose 😭")
    

while is_running:
        
    game_start = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
    
    if game_start == "y":
        cls()
        print(logo)
        user_hand = []
        npc_hand = []
        
        deal_card(card_suitors = user_hand, cards_to_deal = 2)
        deal_card(card_suitors = npc_hand, cards_to_deal = 2)
        
        user_score = total_score(user_hand)
        npc_score = total_score(npc_hand)
        
        print(f"Your cards: {user_hand}, current score: {user_score}")
        print(f"Computer's first card: {npc_hand[0]}")
        
        if user_score == 0:
            print("You win 😎, You have blackjack")
            
        elif npc_score == 0:
            print("You lose 😭, Opponent has blackjack")
            
        elif user_score > 21:
            print("You went over. You lose 😭")
            
        elif npc_score > 21:
            print("Opponent went over. You win 😎")
            
        else:
            another_one = input("Type 'y' to get another card, type 'n' to pass: ")
            if another_one == "y":
                deal_card(user_hand, 1)
                user_score = total_score(user_hand)
                
            while npc_score < 17:
                deal_card(npc_hand, 1)
                npc_score = total_score(npc_hand)
            
            print(f"Your final hand: {user_hand}, final score: {user_score}")
            print(f"Computer's final hand: {npc_hand}, final score: {npc_score}")
            
            compare(user_score, npc_score)
                
    elif game_start == "n":
        is_running = False
        
    else:
        print("Invalid input. Try again")
