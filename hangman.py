from wordfile import w1
from wordfile import w2
from wordfile import w3


import random


level=input("What level of word do you want ?\n")
level=int(level)
if level==1:
  word=random.choice(w1)
elif level==2:
  word=random.choice(w2)
elif level==3:
  word=random.choice(w3)
else:
  print("invalid input")



word=list(word)
print("You have to guess this word.\n","- "*len(word))

answer="_"*len(word)
answer=list(answer)
turns=len(word)+3
while True:
  if turns>0:
   if answer==word:
     print("The word is correct, congratulations")
     break

   guess=input("Enter your guess:  ")

   if guess in word:
     for i in range(len(word)):
       if word[i]==guess:
         answer[i]=guess
         print("Correct guess")
         print(" ".join(answer))
   else:
     turns=turns-1
     print("Wrong guess, please try again")
  else:
    print("Your guessing limit has been finished")
    break
