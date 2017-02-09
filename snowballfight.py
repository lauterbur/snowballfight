import random
import sys
import time

class SnowballFight:
        
        def __init__(self):
                self.hitcounter = 0 ## times you've been hit
                self.penguincounter = 0 ## times you've hit a penguin
                self.skillz = 0
                self.choice = None

        def startFight(self):
                print("You have stumbled into a snowball fight! Quick, duck or throw?")
                self.choice=input().lower()
                if self.choice != "duck" and self.choice != "throw":
                        print("Don't you know how a snowball fight works?")
                        sys.exit()
                else:
                        print("You chose to {}!".format(self.choice))
                return self.choice
        
        def continueFight(self):
                print("Quick, duck or throw?")
                self.choice=input().lower()
                if self.choice != "duck" and self.choice != "throw":
                        print("You didn't duck or throw, what gives?")
                        game.pause()
                        print("The penguins take advantage of your confusion. You're hit!")
                        self.hitcounter += 1
                else:
                        print("You chose to {}!".format(self.choice))
                return self.choice

        def skill(self):
                print("Wait, how good are you at {}ing?".format(self.choice))
                game.pause()
                counter = 0
                oops=["Too late!", "That's not right!", "The penguins are coming!"]
                while counter <5:
                        try:
                                self.skillz=int(input("Enter a number between 1 and 12: "))
                                print(self.skillz)
                                if self.skillz<1 or self.skillz>12:
                                        print("You are eaten by a Gru, smartass.")
                                        sys.exit()
                                else:
                                        print("Watch out for the penguins.")
                                        break
                        except ValueError:
                                if counter == 0:
                                        print("You're running out of time, enter an integer between 1 and 12: ")
                                        counter += 1
                                elif counter >0 and counter !=4:
                                        remaining=4-counter
                                        print(random.choice(oops),remaining)
                                        counter += 1
                                elif counter == 4:
                                        sys.exit("You took too much time to decide, the penguins have overrun your position and declared themselves emporers of the snowpocalypse.")
                return self.skillz

        def throwResult(self):
                throw=random.randint(1,12)
                print("You throw a snowball")
                game.pause()
                if throw-self.skillz > 2 :
                        print("You miss!")
                        game.pause()
                        if random.randint(1,100) % 2 == 0:
                                print("Augh, the penguins hit back! Fear the penguins.")
                                self.hitcounter += 1
                        else:
                                print("You escape retaliation from the penguins... this time.")
                elif throw-self.skillz < -3:
                        print("Your snowball hits! Penguin down, penguin down!")
                        game.pause()
                        self.penguincounter += 1
                        if random.randint(1,100) % 3 == 0:
                                print("Augh, the penguins hit back! Fear the penguins.")
                                self.hitcounter += 1
                        else:
                                print("You escape retaliation from the penguins... this time.")
                else:
                        print("A skua steals your snowball out of the air, scattering the penguins.")

        def duckResult(self):
                duck=random.randint(1,12)
                print("You duck.")
                if duck-self.skillz < -1:
                        print("The penguins miss! Count your lucky skuas.")
                elif duck/self.skillz > -1:
                        print("You're hit!")
                        self.hitcounter += 1

        def pause(self):
                time.sleep(0.5)

if __name__=="__main__":
        game = SnowballFight()
        game.startFight() ## defines self.choice
        game.pause()
        game.skill()  ## defines skillz
        game.pause()
        while game.hitcounter < 5 and game.penguincounter < 5:
                if game.choice == "throw":
                        game.throwResult()
                elif game.choice == "duck":
                        game.duckResult()
                if game.hitcounter == 5 or game.penguincounter == 5:
                        break
                else:        
                        game.pause()
                        game.continueFight()
                game.pause()
        if game.hitcounter == 5:
                print("The penguins are victorious! All hail our penguin overlords.")
                sys.exit()
        elif game.penguincounter == 5:
                print("You have thrown back the penguin hordes. Congratulations.")
                sys.exit()