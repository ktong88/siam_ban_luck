import random

class cardDeck:
    
    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
        self.cards = {}
        self.cards = {
               'orTou'  : [1,2,3,4,5,6,7,8,9,10,11,12,13],
               'angSim' : [1,2,3,4,5,6,7,8,9,10,11,12,13],
               'miHua'  : [1,2,3,4,5,6,7,8,9,10,11,12,13],
               'jiamKak': [1,2,3,4,5,6,7,8,9,10,11,12,13],
            }

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
        #print("score = %d" % score)
        return score

    def porPaiOrNot(self):
        #print("%s turn to decide add card or not" % self.name)
        #print(self.card)
        score = self.calculateScore()
        if (score >= 4):
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
    
    
    def calcWinRate(self):
        """calculate the winning rate based on win_stat"""
        win_count = 0
        tie_count = 0
        lost_count = 0
        total_round = 0
        for i in self.win_stat:
            if (i == 1):
                win_count += 1
            total_round += 1
        
        for i in self.win_stat:
            if (i== 0):
                tie_count += 1
                
        for i in self.win_stat:
            if (i== -1):
                lost_count += 1
        
        #print("%s win count = %d" % (self.name, win_count))
        #print("%s tie count = %d" % (self.name, tie_count))
        #print("%s lost count = %d" % (self.name, lost_count))
        
        return win_count/total_round
    
    def calcWinRatio(self):
        """ calculate win ratio of each player"""
        total = 0
        
        for i in self.win_ratio:
            total += i
        
        #print("%s total win ratio = %d" % (self.name, total))
        
        return (total/(len(self.win_ratio)))
        

class player(human):
    card = {}
    score = 0 # score for current round
    win_stat = []
    win_ratio = []
    bet = 100
    def __init__(self, name):
        self.name = name


class zhong(human):
    card = {}
    score = 0
    win_stat = []
    win_ratio = []
    bet = 100
    def __init__(self,name):
        self.name = name

def distributeCard(deck):
    num_cards = 0


    for k,v in deck.items():
        for n in v:
            num_cards += 1
    print("deck size = %d" % num_cards)
    rand_card = random.randint(1,num_cards)

    #print("rand card = %d" % rand_card)
    num = 1
    for k,v in deck.items():

        for n in v:
            if (num == rand_card):
                return k,n
            else:
                num+=1



def iteration():

    #distribute cards
    x = cardDeck("deck")
    p.card = {}
    p2.card = {}
    p3.card = {}
    z.card = {}
    for i in range(2):
        flower, number = distributeCard(x.cards)

        if flower in p.card:
            p.card[flower].append(number)
        else:
            p.card[flower] = [number]
        x.cards[flower].remove(number)

        flower, number = distributeCard(x.cards)
        if flower in p2.card:
            p2.card[flower].append(number)
        else:
            p2.card[flower] = [number]
        x.cards[flower].remove(number)

        flower, number = distributeCard(x.cards)
        if flower in p3.card:
            p3.card[flower].append(number)
        else:
            p3.card[flower] = [number]
        x.cards[flower].remove(number)
        
        flower, number = distributeCard(x.cards)
        if flower in z.card:
            z.card[flower].append(number)
        else:
            z.card[flower] = [number]
        x.cards[flower].remove(number)


    print("%s card = %s" % (p.name, p.card))
    print("%s card = %s" % (p2.name, p2.card))
    print("%s card = %s" % (p3.name, p3.card))
    print("%s card = %s" % (z.name, z.card))

    def porPai(h):

        getCard = h.porPaiOrNot()

        if(getCard):
            print("%s card before = %s" % (h.name, h.card))
            #flower = (random.choice(list(x.cards)))
            #number = random.choice(x.cards[flower])
            flower, number = distributeCard(x.cards)
            if flower in h.card:
                h.card[flower].append(number)
            else:
                h.card[flower] = [number]
            x.cards[flower].remove(number)
            print("%s card after = %s" %(h.name, h.card))

        else:
            print("%s not getting card" %(h.name))
            pass
        h.score = h.calculateScore()

    porPai(p)
    porPai(p2)
    porPai(p3)
    porPai(z)

    print("%s final score = %d" % (p.name,p.score))
    print("%s final score = %d" % (p2.name, p2.score))
    print("%s final score = %d" % (p3.name, p3.score))
    print("%s final score = %d" % (z.name,z.score))

    if (p.score > z.score):
        print("%s win" % p.name)
        print("%s return = x%d" % (p.name, p.calculateWinReturn()))
        p.win_ratio.append(p.calculateWinReturn())
        p.win_stat.append(1)
        z.win_stat.append(-1)
        #print("%s win stat = %s" % (p.name, p.win_stat))
        #print("%s win stat = %s" % (z.name, z.win_stat))
    elif (p.score == z.score):
        print("tie")
        p.win_stat.append(0)
        z.win_stat.append(0)
        #print("%s win stat = %s" % (z.name, z.win_stat))
        #print("%s win stat = %s" % (p.name, p.win_stat))
    else:
        print("%s win" % z.name)
        print("%s return = x%d" % (z.name, z.calculateWinReturn()))
        p.win_stat.append(-1)
        z.win_stat.append(1)
        z.win_ratio.append(p.calculateWinReturn())
        #print("%s win stat = %s" % (p.name, p.win_stat))
        #print("%s win stat = %s" % (z.name, z.win_stat))

    if (p2.score > z.score):
        print("%s win" % p2.name)
        print("%s return = x%d" % (p2.name, p2.calculateWinReturn()))
        p2.win_ratio.append(p2.calculateWinReturn())
        p2.win_stat.append(1)
        z.win_stat.append(-1)
        # print("%s win stat = %s" % (p2.name, p2.win_stat))
        # print("%s win stat = %s" % (z.name, z.win_stat))
    elif (p2.score == z.score):
        print("tie")
        p2.win_stat.append(0)
        z.win_stat.append(0)
        # print("%s win stat = %s" % (z.name, z.win_stat))
        # print("%s win stat = %s" % (p2.name, p2.win_stat))
    else:
        print("%s win" % z.name)
        print("%s return = x%d" % (z.name, z.calculateWinReturn()))
        p2.win_stat.append(-1)
        z.win_stat.append(1)
        z.win_ratio.append(p2.calculateWinReturn())
        # print("%s win stat = %s" % (p2.name, p2.win_stat))
        # print("%s win stat = %s" % (z.name, z.win_stat))

    if (p3.score > z.score):
        print("%s win" % p3.name)
        print("%s return = x%d" % (p3.name, p3.calculateWinReturn()))
        p3.win_ratio.append(p3.calculateWinReturn())
        p3.win_stat.append(1)
        z.win_stat.append(-1)
        # print("%s win stat = %s" % (p3.name, p3.win_stat))
        # print("%s win stat = %s" % (z.name, z.win_stat))
    elif (p3.score == z.score):
        print("tie")
        p3.win_stat.append(0)
        z.win_stat.append(0)
        # print("%s win stat = %s" % (z.name, z.win_stat))
        # print("%s win stat = %s" % (p3.name, p3.win_stat))
    else:
        print("%s win" % z.name)
        print("%s return = x%d" % (z.name, z.calculateWinReturn()))
        p3.win_stat.append(-1)
        z.win_stat.append(1)
        z.win_ratio.append(p3.calculateWinReturn())
        # print("%s win stat = %s" % (p3.name, p3.win_stat))
        # print("%s win stat = %s" % (z.name, z.win_stat))

    #print(x.cards)


z = zhong("zhong")
p = player("p1")
p2 = player("p2")
p3 = player("p3")

total_round = 10000
#print(x.cards)
for i in range(total_round):
    iteration()

print("%s win rate = %f" % (p.name, p.calcWinRate()))
print("%s win rate = %f" % (p2.name, p2.calcWinRate()))
print("%s win rate = %f" % (p3.name, p3.calcWinRate()))
print("%s win rate = %f" % (z.name, z.calcWinRate()))
print("total round = %d" % total_round)
#print("%s win ratio = %f" % (p.name, p.calcWinRatio()))
#print("%s win ratio = %f" % (z.name, z.calcWinRatio()))
