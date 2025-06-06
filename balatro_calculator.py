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
cards_scored=int(input("cards scored: "))
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
        
class Card:
    def __init__(self,rank,suit,enhancement,edition,has_redseal,is_facecard,is_debuffed):
        self.rank=rank
        self.suit=suit
        self.enhancement=enhancement
        self.edition=edition
        self.has_redseal=has_redseal
        self.is_facecard=is_facecard
        self.is_debuffed=is_debuffed

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
    card=Card((rank,suit,enhancement,edition,redseal,facecard,debuffed))
    played_hand.append(card)

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

#activation type: on score

