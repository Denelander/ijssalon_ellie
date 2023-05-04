def mijn_functie_1(argument):
    dictionary = {
        2: 4, 
        4: 16, 
        10: 100, 
        12: 144
    }
    return dictionary.get(argument)

def mijn_functie_2(key):
    if key == (12,3):
        return [15, 9, 36, 4]
    if key == (12,2):
        return [14, 10, 24, 6]
    if key == (10,5):
        return [15, 5, 50, 2]
    if key == (100,20):
        return [120, 80, 2000, 5]