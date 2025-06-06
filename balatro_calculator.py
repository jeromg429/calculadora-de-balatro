from random import *

mult=0
chips=0

plasma=str(input("playing on plasma deck?(y/n): "))
if plasma=="y": plasma=True
else:plasma=False

observatory=str(input("redmeemed observatory voucher??(y/n): "))
if observatory=="y": observatory=True
else: observatory=False

def fplasma(m,c):
    c=((m+c)/2)**2
    return c

def fobservatory(planetcards,m):
    m*=1.5**planetcards
    return m

handt=str(input("played hand: "))
hands_remaining=int(input("hands remaining: "))
cards_scored=int(input("cards scored: "))
cards_in_hand=int(input("cards in hand: "))
level=int(input("hand level: "))
level-=1

match handt:
    case "high card":
        mult=1+level
        chips=5+(10*level)
    case "pair":
        mult=2+level
        chips=10+(15*level)
    case "two pair":
        mult=2+level
        chips=2+(20*level)
    case "3ok":
        mult=3+(2*level)
        chips=30+(20*level)
    case "straight":
        mult=4+(3*level)
        chips=30+(30*level)
    case "flush":
        mult=4+(2*level)
        chips=35+(15*level)
    case "full house":
        mult=4+(2*level)
        chips=40+(25*level)
    case "4ok":
        mult=7+(3*level)
        chips=60+(30*level)
    case "straight flush":
        mult=8+(4*level)
        chips=100+(40*level)
    case "5ok":
        mult=12+(3*level)
        chips=120+(35*level)
    case "flush house":
        mult=14+(4*mult)
        chips=140+(40*mult)
    case "flush five":
        mult=16+(3*level)
        chips=160+(50*level)
    case _:
        print("error")
        
blind=str(input("is blind boss blind? (y/n): "))
if blind=="n": pass
else:
    bb=str(input("which boss blind?: "))
    if bb== "the arm": 
        if level>1: level-=1
    elif bb== "the flint":
        mult/=2
        chips/=2

played_hand=[]
        
for n in range(1,cards_scored+1):
    print(f"~~~~~ card {n} ~~~~~")
    rank=str(input("card rank: "))
    letter_rank=rank
    if rank=="j" or rank=="q" or rank=="k":rank=10
    elif rank=="a": rank==11
    else: rank=int(rank)
    suit=str(input("card suit: "))
    enhancement=str(input("card enhancement: "))
    edition=str(input("card edition: "))
    if edition=="": edition="normal"
    redseal=str(input("card has redseal? (y/n): "))
    if redseal=="y": redseal=True
    else: redseal==False
    facecard=str(input("is card a facecard? (y/n): "))
    if facecard=="y": facecard=True
    else: facecard==False
    debuffed=str(input("is card debuffed? (y/n): "))
    if debuffed=="y": debuffed=True
    else: debuffed==False
    is_first=""
    if n==1:
        is_first=True
    else:is_first=False
    card=(rank,suit,enhancement,edition,redseal,facecard,debuffed,is_first,letter_rank)
    played_hand.append(card)

in_hand=[]
q_in_hand=0
k_in_hand=0

for n in range(1,cards_in_hand+1):
    print(f"~~~~~ card {n} ~~~~~")
    rank=str(input("card rank: "))
    if rank=="j":rank=10
    elif rank=="q": rank=10 ; q_in_hand+=1
    elif rank=="k": rank=10 ; k_in_hand+=1
    elif rank=="a": rank=11
    else: rank=int(rank)
    
    suit=str(input("card suit: "))
    enhancement=str(input("card enhancement: "))
    edition=str(input("card edition: "))
    if edition=="": edition="normal"
    redseal=str(input("card has redseal? (y/n): "))
    if redseal=="y": redseal=True
    else: redseal==False
    facecard=str(input("is card a facecard? (y/n): "))
    if facecard=="y": facecard=True
    else: facecard==False
    debuffed=str(input("is card debuffed? (y/n): "))
    if debuffed=="y": debuffed=True
    else: debuffed==False
    card=(rank,suit,enhancement,edition,redseal,facecard,debuffed)
    in_hand.append(card)


joker_slots=int(input("how many joker slots? "))
jokers=int(input("how many jokers? "))
joker_list=[]
oops=0
smeared=False
pareidolia=False

for n in range(1,jokers+1):
    print(f"~~~~~ joker #{n} ~~~~~")
    joker=str(input("joker name: "))
    joker_edition=str(input("joker edition: "))
    if joker_edition=="": joker_edition="normal"
    joker=(joker,joker_edition)
    joker_list.append(joker)
    
#and now for my next trick, I will code what *ALL* (score related) jokers in game do... plesase help hahahahhah

#activation type: on played
def f_dna(object): object.append(object[-1])
#retriggers
def f_dusk(phand,handsr):
    if handsr!=1:
        pass
    '''here will go the code for dusk joker when i figure out how to code retriggers lol'''
def f_hack(phand):
    for card in phand:
        if card[0]<=5:
            pass #same as dusk, will code when I figure out how to code retriggers
def f_seltzer(phand):
    phand="placeholder"
    #you guessed it, same as dusk and hack, will code when I figure out how to code retriggers :D
def f_sockandbuskin(phand):
    for card in phand:
        if card[5]==True:
            phand="placeholder"
            #i cant retrigger
def f_hangingchad(phand):
    if phand[7]==True:
        phand="placeholder"
        #i cant retrigger
def f_mime(joker_l,retriggers_hand):
    for joker in joker_l:
        if joker[0]=="mime":
            retriggers_hand+=1
    return retriggers_hand 
#doesnt work rn lol
#modifier jokers:
def f_oopsallsixes(joker_l,oops_value):
    for joker in joker_l:
        if joker[0]=="oops all sixes":
            oops_value+=1
    return oops_value
def f_smearedj(joker_l,smearedvalue):
    for joker in joker_l:
        if joker[0]=="smeared":
            smearedvalue=True
    return smearedvalue
def f_pareidoliav(joker_l,pareidolia_value):
    for joker in joker_l:
        if joker[0]=="pareidolia":
            pareidolia_value=True
    return pareidolia_value
def f_pareidolia(phand,pareidolia_value):
    if pareidolia_value==True:
        for card in phand:
            card[5]=True
        return phand
def f_greedy(pcard,smeared_value,m):
    if smeared_value==False:
        if pcard[1]=="diamonds" or pcard[2]=="wild card":
            m+=5
            return m
    else:
        if pcard[1]=="diamonds" or pcard[1]=="hearts" or pcard[2]=="wild card":
            m+=5
            return m
def f_lusty(pcard,smeared_value,m):
    if smeared_value==False:
        if pcard[1]=="hearts" or pcard[2]=="wild card":
            m+=5
            return m
    else:
        if pcard[1]=="diamonds" or pcard[1]=="hearts" or pcard[2]=="wild card":
            m+=5
            return m
def f_wrathful(pcard,smeared_value,m):
    if smeared_value==False:
        if pcard[1]=="spades" or pcard[2]=="wild card":
            m+=5
            return m
    else:
        if pcard[1]=="spades" or pcard[1]=="clubs" or pcard[2]=="wild card":
            m+=5
            return m
def f_gluttonous(pcard,smeared_value,m):
    if smeared_value==False:
        if pcard[1]=="clubs" or pcard[2]=="wild card":
            m+=5
            return m
    else:
        if pcard[1]=="spades" or pcard[1]=="clubs" or pcard[2]=="wild card":
            m+=5
            return m
def f_fibonacci(pcard,m):
    if pcard[0]==11 or pcard[0]==2 or pcard[0]==3 or pcard[0]==5 or pcard[0]==8:
        m+=8
        return m
def f_scaryface(pcard,c):
    if pcard[5]==True:
        c+=30
        return c
def f_evensteven(pcard,c):
    if pcard[0]%2==0:
        m+=4
        return m
def f_oddtodd(pcard,c):
    if pcard[0]%2!=0:
        c+=31
        return c
def f_scholar(pcard,m,c):
    if pcard[0]==11:
        m+=4
        c+=20
        return (m,c)
def f_photograph(phand,m):
    count=0
    for pcard in phand:
        if pcard[7]==True and pcard[5]==True: count+=1
    m*=2**count
    return m
def f_ancientj(a_suit,smeared_value,pcard,m):
    if smeared_value==False:
        if a_suit==pcard[1] or pcard[2]=="wild card":
            m*=1.5
        return m
    else:
        if a_suit=="hearts" or a_suit=="diamonds":
            if pcard[1]=="hearts" or pcard[1]=="diamonds" or pcard[2]=="wild card":
                m*=1.5
        elif a_suit=="spades" or a_suit=="clubs":  
            if pcard[1]=="spades" or pcard[1]=="clubs" or pcard[2]=="wild card":
                m*=1.5
    return m
def f_walkietalkie(pcard,m,c):
    if pcard[0]==4 or pcard[9]==10:
        m+=4
        c+=10
    return (m,c)
def f_smileyface(pcard,m):
    if pcard[5]==True:
        m+=5
        return m
def f_bloodstone(pcard,oops_value,m):
    if oops_value>0:
        if pcard[1]=="hearts" or pcard[2]=="wild card": m*=1.5
    else: 
        if pcard[1]=="hearts" or pcard[2]=="wild card":
            if 1==random.randint(1,2):m*=1.5
    return m
def f_arrowhead(pcard,smeared_value,c):
    if smeared_value==False:
        if pcard[1]=="clubs" or pcard[2]=="wild card":
            c+=30
    else:
        if pcard[1]=="clubs" or pcard[1]=="spades" or pcard[2]=="wild card":
            c+=30
    return c
def f_onyxagate(pcard,smeared_value,m):
    if smeared_value==False:
        if pcard[1]=="spades" or pcard[2]=="wild card":
            m+=7
    else:
        if pcard[1]=="spades" or pcard[1]=="clubs" or pcard[2]=="wild card":
            m+=7
    return m
def f_idol(pcard,crank,csuit,smeared_value,m):
    if smeared_value==False:
        if (pcard[1]==csuit and pcard[0]==crank) or (pcard[2]=="wild card" and pcard[0]==crank):
            m*=2
            return m
    else:
        if pcard[1]=="hearts" or pcard[1]=="diamonds":
            if (pcard[1]=="hearts" and pcard[0]==crank) or (pcard[1]=="diamonds" and pcard[0]==crank) or (pcard[2]=="wild card" and pcard[0]==crank):
                m*=2
                return m
            elif pcard[1]=="spades" or pcard[1]=="clubs":
                if (pcard[1]=="spades" and pcard[0]==crank) or (pcard[1]=="clubs" and pcard[0]==crank) or (pcard[2]=="wild card" and pcard[0]==crank):
                    m*=2
                    return m
def f_triboulet(pcard,m):
    if pcard[8]=="q" or pcard[8]=="k":
        m*=2
    return m
#activation type: on held
def f_raisedfist(hhand,m):
    temp=[]
    for card in hhand:
        temp.append(card[0])
        temp2=sorted(temp)
        m+=2*temp2[0]
    return m
def f_baron(hcard,m):
    if hcard[8]=="k":
        m*=1.5
    return m
def f_shootthemoon(hcard,m):
    if hcard[8]=="q":
        m+=13
    return m
#activation type: independent
def f_campfire(xm,m):
    m*=xm
    return m
def f_theduo(thand,phand,m):
    if thand=="pair" or thand=="two pair" or thand=="3ok" or thand=="full house" or thand=="4ok" or thand=="5ok" or thand=="flush house" or thand=="flush five":
        m*=2
    elif thand=="straight" or thand=="straight flush" or thand=="flush":
        temp=0
        for card in phand:
            if card[9]==temp:
                m*=2
                return m
            else: temp=card[9]
        return m
def f_thetrio(thand,phand,m):
    if thand=="3ok" or thand=="full house" or thand=="4ok" or thand=="5ok" or thand=="flush house" or thand=="flush five":
        m*=3
    elif thand=="flush":
        temp1=0
        temp2=0
        for card in phand:
            if card[9]==temp1 and card[9]==temp2:
                m*=3
                return m
            else: temp2=temp1 ; temp1=card[9]
        return m
def f_thefamily(thand,phand,m):
    if thand=="4ok" or thand=="5ok" or thand=="flush five":
        m*=4
    elif thand=="flush":
        temp1=0
        temp2=0
        temp3=0
        for card in phand:
            if card[9]==temp1 and card[9]==temp2 and card[9]==temp3:
                m*=4
                return m
            else: temp3=temp2 ; temp2=temp1 ; temp1=card[9]
        return m
def f_thetribe(thand,phand,m):
    if thand=="flush" or thand=="straight flush" or thand=="flush five":
        m*=2
    elif thand=="4ok":
        temp1=""
        temp2=""
        temp3=""
        temp4=""
        for card in phand:
            if card[1]==temp1 and card[1]==temp2 and card[1]==temp3 and card[1]==temp4:
                m*=2
                return m
            else: temp4=temp3 ; temp3=temp2 ; temp2=temp1 ; temp1=card[1]
    return m
def f_theorder(thand,m):
    if thand=="straight flush" or thand=="straight":
        m*=3
    return m
