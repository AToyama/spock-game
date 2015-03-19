# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 18:57:59 2015

@author: André
"""

print ("SPOCK GAME - SHELDON 4EVER")

options = ['rock','paper','scissors','lizard','spock']
import random 

player = int(0)
computer = int(0)

while player < 3 and computer < 3:
       
        a = input("Choose: ")   
        b = random.choice(options)
        print ('Computer choice: ',b)  
        
        if a == b:
            print ("Tie")
                
        if (a == 'scissors'):
             if (b == 'paper'):
                 print ('scissor cuts paper, you win =D')
                 player += 1
                 computer = 0
                 print ('Player Score = ', player)
                 print ("Computer Score = ", computer)
             if (b == 'rock'):
                print("rock crushes scissors, you lose ;-;")
                computer += 1
                player = 0
                print("Player Score", player)
                print("Computer Score", computer)
             if (b == 'lizard'):
                print ("scissors decapitates lizard, you win =D")
                player += 1
                computer = 0
                print ("Player Score", player)
                print ("Computer Score", computer)
             if (b == 'spock'):
                print ("spock smashes scissor, you lose ;-;")
                computer += 1
                player = 0
                print ("Player Score", player)
                print ("Computer Score", computer)
                    
        if (a == 'paper'):
            if (b == 'rock'):
                print ("paper covers rock, you win =D")
                player += 1
                computer = 0
                print ("Player Score", player)
                print ("Computer Score", computer)
            if (b == 'lizard'):
                print ("lizard eats paper, you lose ;-;")
                computer += 1
                player = 0
                print ("Player Score", player)
                print ("Computer Score", computer)
            if (b == 'spock'):
                print ("paper disproves spock, you win =D")
                player += 1
                computer = 0
                print ("Player Score", player)
                print ("Computer Score", computer)
            if (b == 'scissors'):
                print ("scissors cuts paper, you lose ;-;")
                computer += 1
                player = 0
                print ("Player Score", player)
                print ("Computer Score", computer)
                    
        if (a == 'rock'):
            if (b == 'lizard'):
                print ("rock crushes lizard, you win =D")
                player += 1
                computer = 0
                print ("Player Score", player)
                print ("Computer Score", computer)
            if (b == 'spock'):
                print ("spocks desintegrates rock, you lose ;-;")
                computer += 1
                player = 0
                print ("Player Score", player)
                print ("Computer Score", computer)
            if (b == 'scissors'):
                print ("rock crushes scissors, you win")
                player += 1
                computer = 0
                print ("Player Score", player)
                print ("Computer Score", computer)
            if (b == 'paper'):
                print ("paper covers rock, you lose ;-;")
                computer += 1
                player = 0
                print ("Player Score", player)
                print ("Computer Score", computer)
            
        if (a== 'lizard'):
            if (b == 'spock'):
                print ("lizard posion spock, you win =D")
                player += 1
                computer = 0
                print ("Player Score", player)
                print ("Computer Score", computer)
            if (b == 'scissors'):
                print ("scissors decapitates lizard, you lost ;-;")
                computer += 1
                player = 0
                print ("Player Score", player)
                print ("Computer Score", computer)
            if (b == 'paper'):
                print ("lizard eats paper, you win =D")
                player += 1
                computer = 0
                print ("Player Score", player)
                print ("Computer Score", computer)
            if (b == 'rock'):
                print ("rock crushes lizard, you lost ;-;")
                computer += 1
                player = 0
                print ("Player Score", player)
                print ("Computer Score", computer)
            
        if (a == 'spock'):
            if (b == 'scissors'):
                print ("spock smashes scissors, you win =D")
                player += 1
                computer = 0
                print ("Player Score", player)
                print ("Computer Score", computer)
            if (b == 'paper'):
                print ("paper disproves spock, you lose ;-;")
                computer += 1
                player = 0
                print ("Player Score", player)
                print ("Computer Score", computer)
            if (b == 'rock'):
                print ("spock desintegrates rock, you win =D")
                player += 1
                computer = 0
                print ("Player Score", player)
                print ("Computer Score", computer)
            if (b == 'lizard'):
                print ("lizard poisons spock, you lose ;-;")
                computer += 1
                player = 0
                print ("Player Score", player)
                print ("Computer Score", computer)
if (player == 3):
    print ("Congratulations you won!")
elif (computer == 3):
    print ("Defeat, GAME OVER")