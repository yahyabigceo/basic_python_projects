import random,time

player_choice=(input("enter your weapon rock= r paper= p scissor= s :"))
weapons=["r","p","s"]
computer_choice=random.choice(weapons)
print( f'your weapon : {player_choice}')
print( f'opponents weapon :{computer_choice}')
time.sleep(0.5)
if player_choice=='r' and computer_choice=="r":
    print('its a draw!')
elif player_choice=='r'  and computer_choice=="p":
    print('you lose')
elif player_choice=='r'  and computer_choice=="s":
    print('you win !!')
    
if player_choice== 'p' and computer_choice=="r":
    print('you win !')
elif player_choice==  'p' and computer_choice=="p":
    print('its a draw')
elif player_choice=='p' and computer_choice=="s":
    print('you lose !')
    
if player_choice=='s' and computer_choice=="r":
    print('you lose')
elif player_choice=='s' and computer_choice=="p":
    print('you win !!')
    
elif player_choice=='s' and computer_choice=="s":
    print('its a draw')



