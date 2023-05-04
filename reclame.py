from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    smaak = "aardbei"
    prijs = 4
    korting = 0.1
    kortingprijs = prijs - prijs * korting
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak van {smaak}, van {prijs} euro voor {kortingprijs} euro."

def inkomsten_totaal(inkomsten):
    ma = 220
    di = 430
    wo = 125
    do = 160
    vr = 205
    za = 90
    zo = 345
    btw = 0.09
    totaal = ma + di + wo + do + vr + za + zo
    btwtotaal = totaal * btw
    return f"Het totaal van alle inkomsten deze week is {totaal} euro, waarover {btwtotaal} euro btw betaald dient te worden."  

def laag_en_hoog(mijn_lijst):
    mijn_lijst = min(220, 430, 125, 160, 205, 90, 345) and max(220, 430, 125, 160, 205, 90, 345)
    return mijn_lijst 

def gemiddelde(mijn_lijst):
    mijn_lijst = 220 + 430 + 125 + 160 + 205 + 90 + 345
    return f"De gemiddelde inkomsten deze week zijn {mijn_lijst / 7} euro."

def meervoudig(invoer_lijst):
    invoer_lijst = 10, 5, 3, 2, 1, 2, 9
    return invoer_lijst(laag_en_hoog)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer




