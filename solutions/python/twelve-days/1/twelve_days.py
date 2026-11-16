GOODS = (
    "a Partridge in a Pear Tree.",
    "two Turtle Doves, ",
    "three French Hens, ",
    "four Calling Birds, ",
    "five Gold Rings, ",
    "six Geese-a-Laying, ",
    "seven Swans-a-Swimming, ",
    "eight Maids-a-Milking, ",
    "nine Ladies Dancing, ",
    "ten Lords-a-Leaping, ",
    "eleven Pipers Piping, ",
    "twelve Drummers Drumming, ",
)
DAYS = (
            "first",
            "second",
            "third",
            "fourth",
            "fifth",
            "sixth",
            "seventh",
            "eighth",
            "ninth",
            "tenth",
            "eleventh",
            "twelfth"
        )
def recite(start_verse, end_verse):
    song = []
    
    for verse in range(start_verse-1,end_verse):
        if verse == 0:
            present = GOODS[0]
        else:
            present = ''.join(GOODS[verse:0:-1]) + f'and {GOODS[0]}'
            
        song.append(f'On the {DAYS[verse]} day of Christmas my true love gave to me: {present}')

    return song