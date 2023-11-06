#if you don't know how to play blackjack, tbh not super important but look it up anyway LOL
#this script is going to require some googling: I want you to practice using your resources with this one. But of course if you get stuck, reach out :)
'''instructions: randomly generate three values between 1 and 11. in the function bust: add these three numbers together. if they add up to or less than 21, return the sum. If it's over 21, return 0. If it's over 21 BUT there's an 11 as one of the values, return the sum - 10. '''


def add(x, y, z):
    return x + y + z
total = add(4, 6, 9)

if total <= 21:
    print(total)

if total > 21 and total == 21:
    print(0)

if total >21 and total == 12:
    print(10)




    
    
