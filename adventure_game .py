import os
import time #short delay after each line is printed
import random
#adventure game
#Lists of Objects in Game
Places = [ 'Desert', 'Mountain']
desert_Creatures = ['Sphinx', 'Dementor']
mountain_Creatures = ['Dragon', 'Gollum']
Result = ['You Win!', 'You Lose!']
Objects = ['Ring', 'Torch', 'Wings']
#End of list of Objects

"""

FUNCTIONS

"""
def main():
    print('\n')
    print('*' * 20)
    print('Welcome to my game!')
    print('*' * 20)   
    print("1.) Start")
    print("2.) Exit")
    option = input('--> ')
    if option == '1':
        start()
    elif option == '2':
        exit()
    else:
        main() 

#PrintDelay
def print_pause(statement, sec):
    print(statement)
    time.sleep(sec)

#Choice to go to either desert or mountain
def choice ():
        while True:             # Loop continuously
                inp = input("Where would you like to go? (desert or mountain)\n")   # Get the input
                if inp == "desert":  
                        des(random.choice(desert_Creatures),random.choice(Objects))
                        break 
                elif inp == "mountain":
                        moun(random.choice(mountain_Creatures),random.choice(Objects))
                        break
                else: 
                        choice()
                        
#To give choice to play the game again
def restart():
    print('\n')
    print('*' * 20)
    print('Thankyou for Playing my game!')
    print('*' * 20)      
    play_again = input("If you'd like to play again, please type 'yes'\n") #to allow them to play again
    if play_again == "yes":
        main()
    else:
        exit()      
        
#Inside the Mountain
def moun(Creature,Obj):
    print_pause("\nAs you enter the Mountain you obtain " + Obj + " in your inventory.", 3)
    if Creature == 'Gollum':
        print_pause ("In front of you lies a small, slimy, dark creature with pale eyes who eats Goblins and fish, named for the sound he makes when he swallows.", 2)
        print_pause("Gollum is in the habit of speaking to himself in a hissing baby-talk, calling himself \"my precious.\"", 4)
        print_pause("Gollum says, 'To obtain the Holy Grail you have to correctly answer my riddle!'", 5)
        while True: # so will keep looping until user gives correct output
            object_Riddle_1 = (input("Do you choose to use your object to take the Holy Grail or do you choose to answer the riddle? (Ring/Wings/Torch/riddle)\n"))
            if object_Riddle_1 == 'Ring' :
                print_pause("You put the ring on your finger and become invisible.",4)
                print_pause("You manage to sneak past the Gollum and Steal the Holy Grail.", 3)           
                print_pause("The Gollum yells\"Thief, YOU BLOODY THEIFFFFFF, THAT'S MY RING!!!\"", 3)
                print_pause("You use the Holy Grail to teleport to safety!!", 3)          
                print_pause(Result[0], 2) 
                break
                
            elif object_Riddle_1 == 'Wings' :
                print_pause("You put on your Wings .", 2)     
                print_pause("You fly past the Gollum and take the Holy Grail.", 3)                       
                print_pause("The Gollum yells\"Thief, YOU BLOODY THEIFFFFFF!!!\"", 2)
                print_pause("You use the Holy Grail to teleport to safety!!", 3)          
                print_pause(Result[0], 2)
                break
                
                
            elif object_Riddle_1  == 'Torch':
                print_pause("You take out a torch and light it up to scare the Gollum away.", 2)   
                print_pause("Gollum jumps on you and tears you to bits!", 2)
                print_pause("Gollum says,'Delicious!, little human'", 2)
                print_pause(Result[1], 2) 
                break
                
            elif object_Riddle_1 == 'riddle':  
                gollum_Riddle = input("What has roots as nobody sees, Is taller than trees, Up, up, up it goes And yet, never grows? \n")
                if gollum_Riddle == 'Mountains':
                    print_pause("Cracks appear on Gollum's body, as he crumbles to dust and you receive the Holy Grail as reward ",5)
                    print_pause(Result[0], 2)  
                    break
                else:
                    print_pause("Gollum devours you!", 2)
                    print_pause(Result[1], 2) 
                    break
                

    elif Creature == 'Dragon':
        print_pause ("In front of you is a Dragon.", 2)
        print_pause("The Dragon excalims haughtily, \"My armour is like tenfold shields, my teeth are swords, my claws spears, the shock of my tail is a thunderbolt, my wings a hurricane, and my breath death!\"!", 4)
        print_pause("Dragon says, 'To obtain the Holy Grail you have to correctly answer my riddle!'", 5)
        while True:
            object_Riddle_1 = (input("Do you choose to use your object to take the Holy Grail or do you choose to answer the riddle? (Ring/Wings/Torch/riddle)\n"))
            if object_Riddle_1 == 'Ring':
                print_pause("You put the ring on your finger and become invisible.",4)
                print_pause("You manage to sneak past him and steal the Holy Grail!", 2)
                print_pause("You use the Holy Grail to teleport to safety!!", 3)          
                print_pause(Result[0], 2) 
                break
                
            elif object_Riddle_1 == 'Wings':
                print_pause("You put on your Wings and fly.", 2)                     
                print_pause("The Dragon yells \"FLYING WON'T SAVE YOU FROM ME, I AM DEATH ITSELF!!!\"", 3)
                print_pause("Dragon burns you to crisp and devours you!", 2)
                print_pause(Result[1], 2) 
                break
                
            elif object_Riddle_1  == 'Torch':
                print_pause("You take out a torch and light it up to scare the Dragon away.", 2) 
                print_pause("Dragon burns you to crisp and devours you!", 2)
                print_pause(Result[1], 2) 
                break
                
            elif object_Riddle_1 == 'riddle':  
                drag_Riddle = input("For thousands of years, Seen only in tale.\nThe wind as a sail, For one thunderous gale.\nShiny stores rich in lore, The burning temper, like Earth's core.\nWho am I?\n")
                if drag_Riddle == 'Dragon':
                    print_pause("The Dragon melts into the ground and you receive the Holy Grail as reward.",5)
                    print_pause(Result[0], 2)  
                    break
                                      
                else:
                    print_pause("Dragon bites your head off!", 2)
                    print_pause(Result[1], 2) 
                    break              

#Inside the desert
def des(Creature, Obj):
    print_pause("\nAs you enter the Desert you obtain " + Obj + " in your inventory.", 3) 
    if Creature == 'Sphinx':
        print_pause ("In front of you lies a statue with a man's head and a lion's body.", 2)
        print_pause("The mysterious statue is a mystical creature called Sphinx!", 4)
        print_pause("Sphinx says, 'To obtain the Holy Grail you have to correctly answer my riddle!'", 5)
        while True: 
            object_Riddle_1 = (input("Do you choose to use your object to take the Holy Grail or do you choose to answer the riddle? (Ring/Wings/Torch/riddle)\n"))
            if object_Riddle_1 == 'Ring' :
                print_pause("You put the ring on your finger and become invisible.",4)
                print_pause("The Sphinx yells\"YOU CANNOT FOOL ME!!!\"", 2)
                print_pause("Sphinx devours you!", 2)
                print_pause(Result[1], 2) 
                break
                
            elif object_Riddle_1 == 'Wings':
                print_pause("You put on your Wings and fly.", 2)                     
                print_pause("The Sphinx yells\"YOU CANNOT FLY ABOVE ME!!!\"", 2)
                print_pause("Sphinx jumps to you and devours you!", 2)
                print_pause(Result[1], 2) 
                break
                
            elif object_Riddle_1  == 'Torch':
                print_pause("You take out a torch and light it up to scare the creature away.", 2)   
                print_pause("The Sphinx yells\"YOU CANNOT SCARE ME!!!\"", 2)
                print_pause("Sphinx devours you!", 2)
                print_pause(Result[1], 2) 
                break
                
            elif object_Riddle_1 == 'riddle':  
                sphinx_Riddle = input("What is the creature that walks on four legs in the morning, two legs at noon and three in the evening? \n")
                if sphinx_Riddle == 'Man':
                    print_pause("The Sphinx crumbles into dust and you receive the Holy Grail as reward!",5)
                    print_pause(Result[0], 2)   
                    break
                else:
                    print_pause("Sphinx devours you!", 2)
                    print_pause(Result[1], 2)  
                    break
                                         
    
    elif Creature == 'Dementor':
        print_pause ("In front of you lies a gliding, wraithlike Dark creature, widely considered to be one of the foulest to inhabit the world.", 2)
        print_pause ("This mystical creature is called Dementor!", 3)
        print_pause("Dementor says, 'To obtain the Holy Grail you have to correctly answer my riddle!'", 5)
        while True:
            object_Riddle_2 = (input("Do you choose to use your object to take the Holy Grail or do you choose to answer the riddle? (Ring/Wings/Torch/riddle)\n"))
            if object_Riddle_2 == 'Ring' :
                print_pause("You put the ring on your finger and become invisible.",4)
                print_pause("You manage to sneak past the Dementor and Steal the Holy Grail.", 3)
                print_pause("You use the Holy Grail to teleport to safety!!", 3)
                print_pause(Result[0], 2)
                break
                
            elif object_Riddle_2 == 'Wings':
                print_pause("You put on your Wings and fly.", 2)                     
                print_pause("Dementor flies to you and eats your soul!", 2)
                print_pause(Result[1], 2)
                break
                
            elif object_Riddle_2  == 'Torch':
                print_pause("You take out a torch and light it up to scare the creature away.", 2)   
                print_pause("Dementor flies to you and eats your soul!", 2)
                print_pause(Result[1], 2) 
                break
                
            elif object_Riddle_2  == 'riddle':   
                print_pause("What is it?\n", 3)
                dementor_Riddle = input("Voiceless it cries,\nWingless flutters,\nToothless bites,\nMouthless mutters\n")            
                if dementor_Riddle == 'Wind':
                    print_pause("The Dementor screeches in pain and vanishes into the air...",4)
                    print_pause("You receive the Holy Grail as reward!", 4)
                    print_pause(Result[0], 2) 
                    break
                else:
                    print_pause("Dementor flies to you and eats your soul!", 2)
                    print_pause(Result[1], 2) 
                    break                    
        
                                        
#Introduce the Game
def start():
    print_pause("\nWelcome to Adventure Paradox!", 2)
    print_pause("You are a explorer in search of The Holy Grail.", 2)
    print_pause("To get to The Holy Grail you have to beat a BOSS MONSTER, you receive objects that may or may not help you accomplish this depending on the situation.", 5)
    name = input("What is your name explorer? \n")
    time.sleep(2)
    print_pause("Welcome "+ name+ "!", 2)
    print_pause("\nYou are standing at a fork in the road.", 2)
    print_pause("One way leads into the Desert and the other leads to a Mountain.", 4)   
    choice() 
    restart()
    
main()      