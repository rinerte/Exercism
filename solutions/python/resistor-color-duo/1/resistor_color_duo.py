def value(colors):
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
    result = 0
    
    result+= color.index(colors[0]) * 10 + color.index(colors[1])

    return result
        
