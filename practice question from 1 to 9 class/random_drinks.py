#Snapple is a famous tea drink brand from Queens, New York. Each bottle cap
#comes with a silly fun fact.
#Use the random module to create a number from 0 to 5. Then use
#an if/elif/else statement to print out one of these six random Snapple facts:
#0 - 'Flamingos turn pink from eating shrimp.'
#1 - 'The only food that doesn't spoil is honey.'
#2 - 'Shrimp can only swim backwards.'
#3 - 'A taste bud's life span is about 10 days.'
#4 - 'It is impossible to sneeze while sleeping.'
#5 - 'It is illegal to sing off-key in North Carolina.

import random as r
facts = [
    "Flamingos turn pink from eating shrimp.",
    "The only food that doesn't spoil is honey.",
    "Shrimp can only swim backwards.",
    "A taste bud's life span is about 10 days.",
    "It is impossible to sneeze while sleeping.",
    "It is illegal to sing off-key in North Carolina."
]

a=r.randint(0,5)

if a==0:
    print(facts[0])
elif a==1:
    print(facts[1])
elif a==2:
    print(facts[2])
elif a==3:
    print(facts[3])
elif a==4:
    print(facts[4])
elif a==5:
    print(facts[5])
