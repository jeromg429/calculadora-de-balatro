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
    card=(rank,suit,enhancement,edition,redseal,facecard,debuffed)
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
def f_dusk(phand,handsr):
    if handsr!=1:
        pass
    '''here will go the code for dusk joker when i figure out how to code retriggers lol'''
def f_hack(phand):
    for card in phand:
        if card[0]<5:
            pass #same as dusk, will code when I figure out how to code retriggers

#activation type on scored
def f_greedy(pcard,m):
    if pcard[1]=="diamonds":
        m+=5
        return m
def f_lusty(pcard,m):
    if pcard[1]=="hearts":
        m+=5
        return m
def f_wrathful(pcard,m):
    if pcard[1]=="spades":
        m+=5
        return m
def f_gluttonous(pcard,m):
    if pcard[1]=="clubs":
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
