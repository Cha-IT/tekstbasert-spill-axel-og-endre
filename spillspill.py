import random

class Karakter:
    def __init__(self, navn, helse, forsvar, angrep):
        self.navn = navn
        self.helse = helse
        self.forsvar = forsvar
        self.angrep = angrep

spiller = Karakter("Spiller", 10, 0, 3)
fiende1 = Karakter("Fiende1", 3, 0, 3)
fiende2 = Karakter("Fiende1", 3, 1, 4)
fiende3 = Karakter("fiende3", 8, 0, 2)

def seStats(karakter):
    print(f"Name: {karakter.navn}")
    print(f"Health: {karakter.helse}")
    print(f"Attack: {karakter.angrep}")
    print(f"Defense: {karakter.forsvar}")

class Brett:
    def __init__(self, forklaring, valg1, valg2, destinasjon1, destinasjon2, fiende):
        self.forklaring = forklaring
        self.valg1 = valg1
        self.valg2 = valg2
        self.destinasjon1 = destinasjon1
        self.destinasjon2 = destinasjon2
        self.fiende = fiende

brett1 = Brett("Du befinner deg i midten av en skog med to stier forran deg", "høyre", "venstre", "kamp", "neste brett", fiende1)
brett2 = Brett("d", "høyre", "venstre", "neste brett", "kamp", fiende2)
brett3 = Brett("a", "høyre", "venstre", "kamp", "nesteBrett", fiende3)
våreBrett = [brett1, brett2, brett3]
brettnr = 0

def nesteBrett():
    if brettnr == len(våreBrett):
        print("Siste brett")
        return
    nøytral(våreBrett[brettnr])

def nøytral(brett):
    kampStatus = 0
    print(brett.forklaring)
    print("du kan se inventaret ditt ved å skrive se inventar")
    print("du kan velge å enten gå mot", brett.valg1 , "eller mot", brett.valg2)
    while kampStatus == 0:
        brukerInput = input()
        if brukerInput == "seInv" or brukerInput == "se inventar":
            seInv(inventar)
        elif brukerInput == "høyre":
            if brett.destinasjon1 == "kamp":
                kamp(brett.fiende)
                break
            if brett.destinasjon1 == "neste brett":
                brettnr += 1
                nesteBrett()
        elif brukerInput == "venstre":
            if brett.destinasjon2 == "kamp":
                kamp(brett.fiende)
                break
            if brett.destinasjon2 == "neste brett":
                brettnr += 1
                nesteBrett()
        else:
            print("s")

class Item:
    def __init__(self, navn, type, forsvar, angrep):
        self.navn = navn
        self.type = type
        self.forsvar = forsvar
        self.angrep = angrep

smørkniv = Item("smørkniv", "våpen", 0, 1)
kniv = Item("kniv", "våpen", 0, 2)
pistol = Item("pistol", "våpen", 0, 3)
truse = Item("truse", "rustning", 1, 0)
bukse = Item("bukse", "rustning", 2, 0)
items = [smørkniv, kniv, pistol, truse, bukse]
inventar = []
equippedItems = []

def seInv(inventar):
    for i in inventar:
        print(f"{i.navn}, ")

def seEquipped(equippedItems):
    for i in equippedItems:
        print(f"{i.navn}, ")

def PlukkOppItem(item, inventar):
    inventar.append(item)

tilfeldigItem = 0 
def drop(tilfeldigItem, items):
     tilfeldigItem = random.choice(items)
     print("du fikk en", tilfeldigItem.navn)
     PlukkOppItem(tilfeldigItem, inventar)

def equip(item):
    if item in inventar:
        if item.type == "våpen":
            for i in equippedItems:
                if i.type == "våpen":
                    equippedItems.remove(i)
                    spiller.angrep -= i.angrep
                    inventar.append(i)
                    break
            spiller.angrep += item.angrep
            inventar.remove(item)
            equippedItems.append(item)
            print(f"{item.navn} equipped")
        elif item.type == "rustning":
            for i in equippedItems:
                if i.type == "rustning":
                    equippedItems.remove(i)
                    spiller.forsvar -= i.forsvar
                    inventar.append(i)
                    break
            spiller.forsvar += item.forsvar
            inventar.remove(item)
            equippedItems.append(item)
            print(f"{item.navn} equipped")
    else:
        print("item not found in inventory")

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
        global brettnr
        brettnr += 1
        nesteBrett()
    else:
        print("Game Over")

nesteBrett()