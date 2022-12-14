import random

class brett:
    def __init__(self, forklaring, valg1, valg2, destinasjon1, destinasjon2, fiende):
        self.forklaring = forklaring
        self.valg1 = valg1
        self.valg2 = valg2
        self.destinasjon1 = destinasjon1
        self.destinasjon2 = destinasjon2

brett1 = brett("Du befinner deg i midten av en skog med to stier forran deg", "høyre", "venstre", "kamp", "neste brett", "fiende1")
brett2 = brett("d", "høyre", "venstre", "kamp", "neste brett", "fiende1")
våreBrett = [brett1, brett2]
brettnr = 0

def nesteBrett(våreBrett, brettnr):
    nøytral(våreBrett(brettnr))

def nøytral(brett):
    kampStatus = 0
    print(brett.forklaring)
    print("du kan se inventaret ditt ved å skrive, seInv eller se inventar")
    print("du kan velge å enten gå mot", brett.valg1 , "eller mot", brett.valg2)
    while kampStatus == 0:
        brukerInput = input()
        if brukerInput == "seInv" or "se inventar":
            seInv(inventar)
        elif brukerInput == "høyre":
            if brett.destinasjon1 == "kamp":
                kamp(brett.fiende)
                kampStatus = 1
            if brett.destinasjon1 == "neste brett":
                brettnr += 1
                break
        elif brukerInput == "vestre":
            if brett.destinasjon1 == "kamp":
                kamp(brett.fiende)
                kampStatus = 1
            if brett.destinasjon1 == "neste brett":
                brettnr += 1
                break
    nesteBrett()



class karakter:
    def __init__(self, navn, helse, forsvar, angrep):
        self.navn = navn
        self.helse = helse
        self.forsvar = forsvar
        self.angrep = angrep

spiller = karakter("Spiller", 10, 0, 3)
fiende1 = karakter("Fiende1", 3, 0, 3)
fiende2 = karakter("Fiende1", 3, 1, 4)


class Item:
    def __init__(self, navn, type, forsvar, angrep):
        self.navn = navn
        self.type = type
        self.forsvar = forsvar
        self.angrep = angrep

inventar = []
smørkniv = Item("smørkniv", "våpen", 0, 1)
kniv = Item("kniv", "våpen", 0, 2)
pistol = Item("pistol", "våpen", 0, 3)
truse = Item("truse", "rustning", 1, 0)
bukse = Item("bukse", "rustning", 2, 0)
items = [smørkniv, kniv, pistol, truse, bukse]
tilfeldigItem = 0
def PlukkOppItem(item, inventar):
    inventar.append(item)
     
def drop(tilfeldigItem, items):
     tilfeldigItem = random.choice(items)
     print("du fikk en", tilfeldigItem.navn)
     PlukkOppItem(tilfeldigItem, inventar)

def seInv(inventar):
    for i in inventar:
        print(f"{i.navn}, ")

def kamp(fiende):
    spillerHelse = spiller.helse
    fiendeHelse = fiende.helse
    print("Du møtte på", fiende.navn)
    print("Din nåværende helse er", spillerHelse)
    print("Mulige valg: angrip eller løp")
    while spillerHelse > 0 and fiendeHelse > 0:
        brukerInput = input()
        if brukerInput == "angrip":
            if spiller.angrep - fiende.forsvar > 0:
                fiendeHelse -= (spiller.angrep - fiende.forsvar)
            else:
                fiendeHelse -= 1
            print("Fiendens helse ble redusert til", fiendeHelse)
            if fiendeHelse <= 0:
                break
            else:
                if fiende.angrep - spiller.forsvar > 0:
                    spillerHelse -= fiende.angrep - spiller.forsvar
                else:
                    spillerHelse -= 1
                print("Din helse ble redusert til", spillerHelse)
        elif brukerInput == "løp":
            resultat = random.randint(0,1)
            if resultat == 0:
                print("Kampen er over")
                return "løpt"
            else:
                spillerHelse -= fiende.angrep
                print("Du slapp ikke unna, din helse ble redusert til", spillerHelse)
        else:
            print("skriv angrip eller løp")
    if fiendeHelse <= 0:
        print("Du vant kampen!")
        drop(tilfeldigItem, items)
    else:
        print("Game Over")

def stats(karakter):
    print(f"{karakter}sin helse er {karakter.helse}, {karakter}sitt forsvar er {karakter.forsvar}, {karakter}sin helse er {karakter.angrep}")

nesteBrett(våreBrett, brettnr)