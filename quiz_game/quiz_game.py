print("Welcome to the Game!")

playing = input("Do you want to play? ")

if playing.lower()!= "yes":
    quit()

print("Okay, Lets play :) ")

score=0

ans = input("What does CPU stand for? ")

if ans.lower()=="central processing unit":
    print("Correct Answer!")
    score+=1
else:
    print("Incorrect Answer :( ")


ans = input("What does GPU stand for? ")

if ans.lower()=="graphics processing unit":
    print("Correct Answer!")
    score+=1
else:
    print("Incorrect Answer :( ")


ans = input("What does RAM stand for? ")

if ans.lower()=="random access memory":
    print("Correct Answer!")
    score+=1
else:
    print("Incorrect Answer :( ")


ans = input("What doe PSU stand for? ")

if ans.lower()=="power supply unit":
    print("Correct Answer!")
    score+=1
else:
    print("Incorrect Answer :( ")


print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%.")
