def label(colors):
    color = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white"
    ]
    
    suffixes = [
        "",
        "kilo",
        "mega",
        "giga"
    ]

    first = color.index(colors[0])
    second = color.index(colors[1])
    zeros = color.index(colors[2])

    
    result=str(first)
    if first==0:
        result=""
        
    if second == 0:
        zeros+=1
    else:
        result+=str(second*(10**(zeros%3)))

    if first==0 and second==0:
        result = "0"

    result+=" "+suffixes[zeros//3]+"ohms"
    return result
    
    