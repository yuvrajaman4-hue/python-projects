print("Welcome to my computer quiz!")
playing= input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("okay! lets play:)")
score = 0
answer = input("what does CPU stands for? ")
if answer.lower() == "central processing unit":
    print('correct!')
    score+= 1
else:
    print("incorrect!")
    
answer = input("what does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print('correct!')
    score+= 1
else:
    print("incorrect!")
    
answer = input("what does RAM stands for? ")
if answer.lower() == "random access memory":
    print('correct!')
    score+= 1
else:
    print("incorrect!")
    
answer = input("what does ROM stands for? ")
if answer.lower() == "read only memory":
    print('correct!')
    score+= 1
else:
    print("incorrect!")
    
answer = input("what does www stands for? ")
if answer.lower() == "world wide web":
    print('correct!')
    score+= 1
else:
    print("incorrect!")

print("you got "+ str(score) +" questions correct!")
print("you got "+ str((score/5)*100) + "%")
    