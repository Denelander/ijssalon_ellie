prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
}

aanbieding = prijzen["aardbei"] *0.8

reclame_tekst = f"vandaag in de aanbieding: vanille-ijs, 1 liter - slechts €{aanbieding}"

reclame_tekst2 = reclame_tekst[:3]

reclame_tekst3 = f"VANDAAG IN DE AANBIEDING: VANILLE-IJS, 1 LITER - SLECHTS €{aanbieding}"

reclame_tekst4 = [f"VANDAAG", "IN", "DE", "AANBIEDING:", "VANILLE-IJS,", 1, "LITER", " - ", "SLECHTS", "€", {aanbieding}]

for el in reclame_tekst4:
    if el >= 5:  
    print(el.upper())
    if el <= 5:
    print(el.lower())
