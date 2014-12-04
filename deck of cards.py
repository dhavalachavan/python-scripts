import itertools, random

deck = list(itertools.product(range(1,14),['Spade','Black','Club','Diamond']))

random.shuffle(deck) 

for i in range(5):
     print ('You got',deck[i][0],'of',deck[i][1])


M1411020112016742


