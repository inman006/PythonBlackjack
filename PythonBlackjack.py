#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import random
import time

from colorama import Fore

### HELPER FUNCTIONS (IF NECESSARY) ###
def play_hand(purse, deck):
  
  time.sleep(1)
  
  #Values:
  facecards = ['J', 'Q', 'K']
  
  p_score = 0
  d_score = 0

  select_deck = deck
  
  dealer1 = random.choice(deck)
  
  if dealer1.isnumeric() == True:
    d_score += int(dealer1)
  
  elif dealer1 in facecards:
    d_score += 10
  
  else:
    if d_score <= 10:
      d_score += 11
  
    else:
      d_score += 1  
  
  deck.remove(dealer1)
  
  deck.append(random.choice(select_deck))
  
  player1 = random.choice(deck)
  
  if player1.isnumeric() == True:
    p_score += int(player1)
  
  elif player1 in facecards:
    p_score += 10
  
  else:
    if p_score <= 10:
      p_score += 11
  
    else:
      p_score += 1  
  
  deck.remove(player1)
  
  deck.append(random.choice(select_deck))
  
  dealer2 = random.choice(deck)
  
  if dealer2.isnumeric() == True:
    d_score += int(dealer2)
  
  elif dealer2 in facecards:
    d_score += 10
  
  else:
    if d_score <= 10:
      d_score += 11
  
    else:
      d_score += 1  
  
  deck.remove(dealer2)
  
  deck.append(random.choice(select_deck))
  
  player2 = random.choice(deck)
  
  if player2.isnumeric() == True:
    p_score += int(player2)
  
  elif player2 in facecards:
    p_score += 10
  
  else:
    if p_score <= 10:
      p_score += 11
  
    else:
      d_score += 1  
  
  deck.remove(player2)
  
  deck.append(random.choice(select_deck))

  d_hand_start = ['?', dealer2]
  
  d_hand = [dealer1, dealer2]
  
  p_hand = [player1, player2]

  bet = input(Fore.WHITE + '\nPlease place a bet:\n\n' + Fore.YELLOW)
  
  pot = int(bet) * 2
  
  purse = str(int(purse) - int(bet))
  
  while bet.isnumeric() == False:
  
    print(Fore.RED +'\nError: non-numeric entry detected')
  
    bet = input(Fore.WHITE +'\nPlease place abet:\n\n' + Fore.YELLOW)
  
    pot = int(bet) * 2
  
    purse = str(int(purse) - int(bet))

  print(Fore.WHITE + '\nPurse:' + purse + '    Bet:' + str(bet) + '    Pot:' + str(pot))
  
  time.sleep(1)

  print(Fore.WHITE + '''
█▀▄ █▀▀ ▄▀█ █░░ █ █▄░█ █▀▀   █▀▀ ▄▀█ █▀█ █▀▄ █▀ ░ ░ ░
█▄▀ ██▄ █▀█ █▄▄ █ █░▀█ █▄█   █▄▄ █▀█ █▀▄ █▄▀ ▄█ ▄ ▄ ▄''')
  
  time.sleep(1)

  print(Fore.WHITE + '''
    Dealer Cards = ''' + str(d_hand_start) + '''
    Player Cards = ''' + str(p_hand))
  
  if p_score == 21:
    
    print(Fore.GREEN + '''
█▄▄ █░░ ▄▀█ █▀▀ █▄▀ ░░█ ▄▀█ █▀▀ █▄▀ █   █▄█ █▀█ █░█   █░█░█ █ █▄░█ █
█▄█ █▄▄ █▀█ █▄▄ █░█ █▄█ █▀█ █▄▄ █░█ ▄   ░█░ █▄█ █▄█   ▀▄▀▄▀ █ █░▀█ ▄''')

    purse = int(purse) + int(pot)
  
    print(Fore.WHITE + '\nPurse:' + str(purse) + '    Bet:' + str(bet) + '    Pot:' + str(pot))
  
    return purse
    
  print(Fore.WHITE + '\nPlayer Score:' + str(p_score) + '    Dealer Score: ?')
  
  time.sleep(1)

  choice = input('\nHit or Stay? ' + Fore.RED)

  while choice.upper() == 'HIT' or choice.upper() == 'H':
  
    new_card = random.choice(select_deck)
  
    p_hand.append(new_card)
  
    if new_card.isnumeric() == True:
      p_score += int(new_card)
  
    elif new_card in facecards:
      p_score += 10
  
    else:
      if p_score <= 10:
        p_score += 11
  
      else:
        p_score += 1  
    deck.remove(new_card)
  
    deck.append(random.choice(select_deck))

    if p_score > 21:
  
      print(Fore.WHITE + '''
    Dealer Cards = ''' + str(d_hand_start) + '''
    Player Cards = ''' + str(p_hand))
  
      print(Fore.WHITE + '\nPlayer Score:' + Fore.RED + str(p_score) + Fore.WHITE +'    Dealer Score: ?')

      time.wait(1)

      print(Fore.RED + '''
█▀█ █░█ ░   █▄░█ █▀█ █   █▄▄ █░█ █▀ ▀█▀ █
█▄█ █▀█ █   █░▀█ █▄█ ▄   █▄█ █▄█ ▄█ ░█░ ▄''')
      
      time.wait(1)
      
      print(Fore.WHITE + '\nPurse:' + str(purse) + '    Bet:' + str(bet) + '    Pot:' + str(pot))
  
      return purse
  
    elif p_score == 21:
  
      print('\n21 exactly!')
  
      print(Fore.YELLOW + '\nCan the dealer catch?' + Fore.WHTIE)
  
      time.sleep(1)
  
      while p_score >= d_score and d_score <= 17:
  
        new_dealer = random.choice(select_deck)
  
        d_hand.append(new_dealer)
  
        if new_dealer.isnumeric() == True:
          d_score += int(new_dealer)
  
        elif new_dealer in facecards:
          d_score += 10
  
        else:
          if d_score <= 10:
            d_score += 11
  
          else:
            d_score += 1  
  
        deck.remove(new_dealer)
  
        deck.append(random.choice(select_deck))

        print('''
    Dealer Cards = ''' + str(d_hand)+ '''
    Player Cards = ''' + str(p_hand))
  
        print('\nPlayer Score:' + str(p_score) + '    Dealer Score:' + str(d_score))
  
        time.sleep(1)
  
        if d_score > 21:
  
          print(Fore.GREEN + '''
█▄█ █▀█ █░█   █░█░█ █ █▄░█ █
░█░ █▄█ █▄█   ▀▄▀▄▀ █ █░▀█ ▄''')

          purse = int(purse) + int(pot)

          print(Fore.WHITE + '\nPurse:' + str(purse) + '    Bet:' + str(bet) + '    Pot:' + str(pot))

          return purse

        if p_score > d_score:

          print(Fore.GREEN + '''
█▄█ █▀█ █░█   █░█░█ █ █▄░█   ▀█▀ █░█ █ █▀   █░█ ▄▀█ █▄░█ █▀▄
░█░ █▄█ █▄█   ▀▄▀▄▀ █ █░▀█   ░█░ █▀█ █ ▄█   █▀█ █▀█ █░▀█ █▄▀ ▄''')

          purse = int(purse) + int(pot)

          print(Fore.WHITE + '\nPurse:' + str(purse) + '    Bet:' + str(bet) + '    Pot:' + str(pot))

          return purse

        elif p_score == d_score:

          print(Fore.WHITE + '''
█░░ █▀█ █▀█ █▄▀ █▀   █░░ █ █▄▀ █▀▀   ▄▀█   █▀█ █░█ █▀ █░█ ░
█▄▄ █▄█ █▄█ █░█ ▄█   █▄▄ █ █░█ ██▄   █▀█   █▀▀ █▄█ ▄█ █▀█ ▄''')

          purse = int(purse) + int(bet)

          print(Fore.WHITE + '\nPurse:' + str(purse) + '    Bet:' + str(bet) + '    Pot:' + str(pot))

          return purse    

    print(Fore.WHITE + '''

    Dealer Cards = ''' + str(d_hand_start) + '''

    Player Cards = ''' + str(p_hand))

    time.sleep(1)

    print('\nPurse:' + purse + '    Bet:' + str(bet) + '    Pot:' + str(pot))

    time.sleep(1)

    print('\nPlayer Score:' + str(p_score) + '    Dealer Score: ?')

    time.sleep(1)

    choice = input('\nHit or Stay? ' + Fore.RED)

  print(Fore.WHITE + '''
    Dealer Cards = ''' + str(d_hand)+ '''
    Player Cards = ''' + str(p_hand))

  print('\nPlayer Score:' + str(p_score) + '    Dealer Score:' + str(d_score))

  time.sleep(1)
  
  if p_score >= d_score:

    print(Fore.GREEN +'\nCan the dealer catch?' + Fore.WHITE)

    time.sleep(1)

    while p_score >= d_score and d_score <= 21:

      new_dealer = random.choice(select_deck)

      d_hand.append(new_dealer)

      if new_dealer.isnumeric() == True:
        d_score += int(new_dealer)

      elif new_dealer in facecards:
        d_score += 10

      else:
        if d_score <= 10:
          d_score += 11

        else:
          d_score += 1  

      deck.remove(new_dealer)

      deck.append(random.choice(select_deck))

      print('''
    Dealer Cards = ''' + str(d_hand)+ '''
    Player Cards = ''' + str(p_hand))

      print('\nPlayer Score:' + str(p_score) + '    Dealer Score:' + str(d_score))

      time.sleep(1)

      if d_score > 21:
        print(Fore.GREEN + '''
█▀▄ █▀▀ ▄▀█ █░░ █▀▀ █▀█   █▄▄ █░█ █▀ ▀█▀ █▀ █
█▄▀ ██▄ █▀█ █▄▄ ██▄ █▀▄   █▄█ █▄█ ▄█ ░█░ ▄█ ▄ ''')

        purse = int(purse) + int(pot)

        print(Fore.WHITE + '\nPurse:' + str(purse) + '    Bet:' + str(bet) + '    Pot:' + str(pot))

        return purse

  if p_score > d_score:
    print(Fore.GREEN + '''
█▄█ █▀█ █░█   █░█░█ █ █▄░█ █ 
░█░ █▄█ █▄█   ▀▄▀▄▀ █ █░▀█ ▄''')

    purse = int(purse) + int(pot)

    print(Fore.WHITE + '\nPurse:' + str(purse) + '    Bet:' + str(bet) + '    Pot:' + str(pot))

    return purse

  else:
    print(Fore.RED + '''
█▀▄ █▀▀ ▄▀█ █░░ █▀▀ █▀█   █░█░█ █ █▄░█ █▀ ░
█▄▀ ██▄ █▀█ █▄▄ ██▄ █▀▄   ▀▄▀▄▀ █ █░▀█ ▄█ ▄''')

    print(Fore.WHITE + '\nPurse:' + str(purse) + '    Bet:' + str(bet) + '    Pot:' + str(pot))

    return purse
  


### MAIN FUNCTION ###
def main():
  
  print('''
    Welcome to...''')
  
  time.sleep(1)

  print(Fore.YELLOW + '''
  ▒█▀▀█ █░░█ ▀▀█▀▀ █░░█ █▀▀█ █▀▀▄  
  ▒█▄▄█ █▄▄█ ░░█░░ █▀▀█ █░░█ █░░█   
  ▒█░░░ ▄▄▄█ ░░▀░░ ▀░░▀ ▀▀▀▀ ▀░░▀ ''')
  
  time.sleep(1)

  print('''
      ▒█▀▀█ █░░ █▀▀█ █▀▀ █░█ ░░░▒█ █▀▀█ █▀▀ █░█ 
      ▒█▀▀▄ █░░ █▄▄█ █░░ █▀▄ ░▄░▒█ █▄▄█ █░░ █▀▄ 
      ▒█▄▄█ ▀▀▀ ▀░░▀ ▀▀▀ ▀░▀ ▒█▄▄█ ▀░░▀ ▀▀▀ ▀░▀''')
  
  time.sleep(1)
  
  print(Fore.WHITE + '''
            Created by Ryan Inman''')
  

  new_deck = ['A', 'A', 'A', 'A', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4',
  '4', '4', '5', '5', '5', '5', '6', '6', '6', '6', '7', '7', '7', '7', 
  '8', '8', '8', '8', '9', '9', '9', '9', '10', '10', '10', '10', 'J', 'J', 
  'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K']
  
  random.shuffle(new_deck)
  
  time.sleep(1)
  
  purse = input(Fore.WHITE + '\nPlease enter your beginning purse value:\n\n' + Fore.GREEN)
  
  time.sleep(1)
  
  print(Fore.YELLOW + '\nCha-ching! '+ Fore.WHITE + purse + ' bucks added to your purse!')
  
  time.sleep(1)

  print(Fore.WHITE + '''
█░░ █▀▀ ▀█▀ ▀ █▀   █▀█ █░░ ▄▀█ █▄█ █
█▄▄ ██▄ ░█░ ░ ▄█   █▀▀ █▄▄ █▀█ ░█░ ▄''')
  
  while purse.isnumeric() == False:
    print(Fore.RED + '\nError: non-numeric entry detected')
    purse = input(Fore.WHITE + '\nease enter your beginning purse value:\n\n')
  
  while int(purse) > 0:
    purse = play_hand(purse, new_deck)

  print(Fore.WHITE + 'Purse empty...')
  
  time.sleep(1)
  
  print(Fore.RED + '''
█▀▀ ▄▀█ █▀▄▀█ █▀▀   █▀█ █░█ █▀▀ █▀█ ░
█▄█ █▀█ █░▀░█ ██▄   █▄█ ▀▄▀ ██▄ █▀▄ ▄''')

    

### DUNDER CHECK ###
if __name__ == "__main__":
  main()
