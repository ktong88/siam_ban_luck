import random
import pysnooper

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
    #@pysnooper.snoop()
    def calculateWinReturn(self):
        """return the win bet based on flower and card count"""
        cardCount = 0
        #print(self.card)
        if (len(self.card.keys()) == 1):
            #same flower
            for k,v in self.card.items():
                for n in v:
                    cardCount += 1
            if (cardCount == 2):
                return 2
            elif (cardCount == 3):
                return 3
        else:
            return 1
    
    
    def calcWinRate(self, win_stat):
        """calculate the winning rate based on win_stat"""
        win_count = 0
        tie_count = 0
        lost_count = 0
        total_round = 0
        for i in win_stat:
            if (i == 1):
                win_count += 1
            total_round += 1
        
        for i in win_stat:
            if (i== 0):
                tie_count += 1
                
        for i in win_stat:
            if (i== -1):
                lost_count += 1
        
        #print("%s win stat = %s" % (self.name, win_stat))
        print("%s win count = %d" % (self.name, win_count))
        print("%s tie count = %d" % (self.name, tie_count))
        print("%s lost count = %d" % (self.name, lost_count))
        
        return win_count/(win_count+lost_count)
    
    def calcWinRatio(self, win_ratio):
        """ calculate win ratio of each player"""
        total = 0
        
        for i in win_ratio:
            total += i
        
        #print("%s win ratio = %s" % (self.name, win_ratio))
        #print("%s total win ratio = %d" % (self.name, total))
        
        return (total/(len(win_ratio)))
        

class player(human):
    
    
    
    
    def __init__(self, name):
        self.name = name
        self.__win_stat = []
        self.__score = 0 # score for current round
        self.__card = {}
        self.__win_ratio = []
        self.__bet = 100


class zhong(human):
    
    def __init__(self,name):
        self.name = name
        self.__card = {}
        self.__score = 0
        self.__win_stat = []
        self.__win_ratio = []
        self.__bet = 100

def distributeCard(deck):
    num_cards = 0


    for k,v in deck.items():
        for n in v:
            num_cards += 1
    #print("deck size = %d" % num_cards)
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
    for p in player_list:
        p.card = {}
    z.card = {}
    for i in range(2):
        
        for p in player_list:
            flower, number = distributeCard(x.cards)
            if flower in p.card:
                p.card[flower].append(number)
            else:
                p.card[flower] = [number]
            x.cards[flower].remove(number)
        
        flower, number = distributeCard(x.cards)
        if flower in z.card:
            z.card[flower].append(number)
        else:
            z.card[flower] = [number]
        x.cards[flower].remove(number)

    #for p in player_list:
        #print("%s card = %s" % (p.name, p.card))
    #print("%s card = %s" % (z.name, z.card))

    def porPai(h):

        getCard = h.porPaiOrNot()

        if(getCard):
            #print("%s card before = %s" % (h.name, h.card))
            flower, number = distributeCard(x.cards)
            if flower in h.card:
                h.card[flower].append(number)
            else:
                h.card[flower] = [number]
            x.cards[flower].remove(number)
            #print("%s card after = %s" %(h.name, h.card))

        else:
            #print("%s not getting card" %(h.name))
            pass
        h.score = h.calculateScore()

    for p in player_list:
        porPai(p)
    porPai(z)

    #for p in player_list:
    #    print("%s final score = %d" % (p.name,p.score))
    #print("%s final score = %d" % (z.name,z.score))

    for p in player_list:
        zhong_card_count = 0
        player_card_count = 0
        for k,v in z.card.items():
            for n in v:
                zhong_card_count += 1
        for k,v in p.card.items():
            for n in v:
                player_card_count += 1
                
        if (z.score >= 8 and zhong_card_count == 2 and player_card_count == 3):
            #print("%s win" % z.name)
            #print("%s return = x%d" % (z.name, z.calculateWinReturn()))
            p._player__win_stat.append(-1)
            z._zhong__win_stat.append(1)
            z._zhong__win_ratio.append(p.calculateWinReturn())
        elif (p.score >= 8 and zhong_card_count == 3 and player_card_count == 2):
            #print("%s win" % p.name)
            #print("%s return = x%d" % (p.name, p.calculateWinReturn()))
            p._player__win_ratio.append(p.calculateWinReturn())
            p._player__win_stat.append(1)
            z._zhong__win_stat.append(-1)
        elif (p.score > z.score):
            #print("%s win" % p.name)
            #print("%s return = x%d" % (p.name, p.calculateWinReturn()))
            p._player__win_ratio.append(p.calculateWinReturn())
            p._player__win_stat.append(1)
            z._zhong__win_stat.append(-1)
        elif (p.score == z.score):
            #print("%s tie" % p.name)
            p._player__win_stat.append(0)
            z._zhong__win_stat.append(0)
        else:
            #print("%s win" % z.name)
            #print("%s return = x%d" % (z.name, z.calculateWinReturn()))
            p._player__win_stat.append(-1)
            z._zhong__win_stat.append(1)
            z._zhong__win_ratio.append(p.calculateWinReturn())

    


z = zhong("zhong")
player_list = []
for i in range(5):
    name = "p" + str(i)
    player_list.append(player(name))



total_round = 10000
for i in range(total_round):
    iteration()

for p in player_list:
    print("========================================")
    print("%s win rate = %f" % (p.name, p.calcWinRate(p._player__win_stat)))
    print("%s win ratio = %f" % (p.name, p.calcWinRatio(p._player__win_ratio)))
print("========================================")
print("%s win rate = %f" % (z.name, z.calcWinRate(z._zhong__win_stat)))
print("%s win ratio = %f" % (z.name, z.calcWinRatio(z._zhong__win_ratio)))
print("========================================")
print("total round = %d" % total_round)


