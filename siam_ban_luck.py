import random

class cardDeck:

    cards = {
               'orTou'  : [1,2,3,4,5,6,7,8,9,10,11,12,13],
               'angSim' : [1,2,3,4,5,6,7,8,9,10,11,12,13],
               'miHua'  : [1,2,3,4,5,6,7,8,9,10,11,12,13],
               'jiamKak': [1,2,3,4,5,6,7,8,9,10,11,12,13],
            }
    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

class human:
    def __init__(self, name):
        self.name = name
    def calculateScore(self):
        score = 0
        ori_v = 0
        for k,v in self.card.items():
            for s in v:
                if (s > 10):
                    ori_v = s
                if (s == 11):
                    s -= 1
                elif (s == 12):
                    s -= 2
                elif (s == 13):
                    s -= 3
                score += s
                s = ori_v
        score = score % 10
        print("score = %d" % score)
        return score

    def porPaiOrNot(self):
        print("%s turn to decide add card or not" % self.name)
        print(self.card)
        score = self.calculateScore()
        if (score >= 6):
            return 0
        else :
            return 1
    def calculateWinReturn(self):
        """return the win bet based on flower and card count"""
        cardCount = 0
        if (list(self.card) == 1):
            #same flower
            for k,v in self.card.items():
                cardCount += 1
            if (cardCount == 2):
                return 2
            elif (cardCount == 3):
                return 3
        else:
            return 1
                

class player(human):
    card = {}
    score = 0
    def __init__(self, name):
        self.name = name


class zhong(human):
    card = {}
    score = 0
    def __init__(self,name):
        self.name = name

x = cardDeck
z = zhong("zhong")
p = player("p1")

print(x.cards)


#distribute cards
for i in range(2):
    flower = (random.choice(list(x.cards)))
    number = random.choice(x.cards[flower])
    if flower in p.card:
        p.card[flower].append(number)
    else:
        p.card[flower] = [number]
    x.cards[flower].remove(number)

    flower = (random.choice(list(x.cards)))
    number = random.choice(x.cards[flower])
    if flower in z.card:
        z.card[flower].append(number)
    else:
        z.card[flower] = [number]
    x.cards[flower].remove(number)


print("%s card = %s" % (p.name, p.card))
print("%s card = %s" % (z.name, z.card))

def porPai(h):

    getCard = h.porPaiOrNot()

    if(getCard):
        print("%s card before = %s" % (h.name, h.card))
        flower = (random.choice(list(x.cards)))
        number = random.choice(x.cards[flower])
        if flower in h.card:
            h.card[flower].append(number)
        else:
            h.card[flower] = [number]
        x.cards[flower].remove(number)
        print("%s card after = %s" %(h.name, h.card))

    else:
        print("not getting card")
    h.score = h.calculateScore()

porPai(p)
porPai(z)

print("%s final score = %d" % (p.name,p.score))
print("%s final score = %d" % (z.name,z.score))

if (p.score > z.score):
    print("%s win" % p.name)
    print("%s return = x%d" % (p.name, p.calculateWinReturn()))
elif (p.score == z.score):
    print("tie")
else:
    print("%s win" % z.name)
    print("%s return = x%d" % (z.name, z.calculateWinReturn()))

print(x.cards)
