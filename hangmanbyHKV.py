import string
import random
print("Are you ready to play Hangman ?")
x=input("Enter yes to start :")
y=x.lower()
if y=="yes":
    name=input("Enter name :")
    print("Hello",name,".It's time to play hangman!")
    print("You have to guess the word otherwise you will be hanged, you will have 15 turns.")
    print("Be warned this can be tough.")
    print("Just don't enter same character more than once")
    while y=="yes":
        list1=["sister","mansion","brainwash","microsoft","playstation","management","secret","house","desktop","warriors","player","unknown","battlegrounds","january","influence","submerge","agriculture",'sportscar',"science","matrix","clock","playlist","addition","fantastic","technology","foundation","amsterdam","america","alabama","memorial","kowalski","analysis"]
        n=random.randrange(len(list1))
        word=list1[n]
        list2=list(word) #word converted to list
        list3=[]#empty list
        s=[]
        d=[]
        sde=[]
        for k in list2:
            if k not in s:
                s.append(k)
        turns=15
        correctguesses=0
        v=0
        f=0
        print("The new word is :")
        for i in range(len(word)):
            list3.append("_")#adding dashes to new list
        for j in list3:
            print(j," ",end="")
        print()
        while turns > 0:
            char=input("Enter character:")
            r=char.lower()      
            for i in range(len(list3)):
                if list2[i]==r:
                    list3[i]=r        
            if r in d:
                print()
                print("Error: input values repeated ")
                f+=1
                print()
                turns-=1
            elif r=="":
                print()
                print("Error: no input ")
                f+=1
                print()
                turns-=1      
            else:
                if v==0:
                    for g in list3:
                        print(g," ",end="")
                if r in list2:
                    print("Character found in word.")
                    correctguesses+=1
                    d.append(r)
                elif r=="im slav":
                    v+=1
                    print()
                    print("--------------------------------------------------------------------------------------------------------------------")
                    print("          Say no more blin, you have won, have some vodka.")
                    print("--------------------------------------------------------------------------------------------------------------------")
                    break
                else:
                    print("character not in word !!!, try again.")
            turns-=1
            if correctguesses==len(s):
                print("--------------------------------------------------------------------------------------------------------------------")
                print("                      You won")
                print("              but you won't, next time !")
                print("--------------------------------------------------------------------------------------------------------------------")
                break
            else:
                print("turns left:",turns)
        if correctguesses!=len(s)and v==0 and f==0:
            print("--------------------------------------------------------------------------------------------------------------------")
            print("                          YOU Hanged !!")
            print("The word was:")
            print(list1[n])
            print("--------------------------------------------------------------------------------------------------------------------")
        x=input("Enter yes to restart , anything else to quit:")
        y=x.lower()
        print()
else:
    print("Am i a joke to you?")
    print("Blin, all you had to was follow my instructions !!!")#CJ
    
