
    

word = "Hello"
for x in range(8):
    print(word)
        
#What about as a while loop?
word = "Hello"
i = 0
while i < 8:
    print(word)
    i = i +1

        
    
#The loop iterations are one behind in a non-programming counting way... how can we fix this?
count = 1
while (count < 3):
    print("While loop iteration", count)
    count = count + 1
        
#Same deal here!
for x in range(3):
    print("For loop iteration:", x + 1)

#Uh oh I messed up and made an infinite loop... so silly of me!
endless = 6
while (endless < 5):
    print("I'm stuck in this loop!!!!")
    
#print out your last name one letter at a time
list = ("p", "a", "l", "m", "a")
for x in (list):
    print(x)
       
#aw i suck i made another infinite loop.. use that thing I taught you about to get out once it prints once... starts with a b... br....
found = False
while found == False:
    print("i only printed once")
    found = True
        
#can you fill this out so that it prints found when it hits the letter r?
for x in "Marist":
    if x == 'r':
        print("found")


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list)

