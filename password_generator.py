# created by aniket0511
#a random password generator
import random
l=[] #empty list
for i in range(65,91):
    l.append(chr(i)) #char 'A' to 'Z'

for i in range(97,123):
    l.append(chr(i)) #char 'a' to 'z'

for i in range(35,39):
    l.append(chr(i)) #special char '#','$','%','&'

l.append(chr(42)) #char '*'
l.append(chr(64)) #char '@'

#password of length 7
x=random.choice(l)
for i in range(6):
    x=x+random.choice(l)

print("Your password is:")
print(x)

print("Please upvote if you like it!")



