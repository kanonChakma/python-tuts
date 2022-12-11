def showScore(count):
    print ("Your Score is ",count)

print("Welcome to the app: ")
res = input("Do You Want to Play the Quiz: ")

if res.lower() != "yes":
    quit()
print("Let's start play :)")
count = 0

ans = input("What does cpu stand for? ")
if ans == 'central pocessing unit':
    print("Correct")
    count+=1
    showScore(count)
else:
    print("inCorrect")

ans = input("What does gpu stand for? ")
if ans == 'graphic pocessing unit':
    print("Correct")
    count+=1
    showScore(count)
else:
    print("inCorrect")


ans = input("What does psu stand for? ")
if ans == 'power supply unit':
    print("Correct")
    count+=1
    showScore(count)
else:
    print("inCorrect")





