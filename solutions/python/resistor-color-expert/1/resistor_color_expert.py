def resistor_label(bands):
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
    tolerance_color = [
        "grey",
        "violet",
        "blue",
        "green",
        "brown",
        "red",
        "gold",
        "silver"
    ]
    tolerance_value = [
        "±0.05%",
        "±0.1%",
        "±0.25%",
        "±0.5%",
        "±1%",
        "±2%",
        "±5%",
        "±10%"
    ]
    if len(bands)<4:
        return "0 ohms"
    if len(bands)==4:
        value = (color.index(bands[0])*10+color.index(bands[1]))*(10**color.index(bands[2]))
    else:
        value = (color.index(bands[0])*100+color.index(bands[1])*10+color.index(bands[2]))*(10**color.index(bands[3]))

    suffix = ""

    if value>=1000000000:
        value = value/1000000000
        suffix = "giga"
    elif value>=1000000:
        value = value/1000000
        suffix = "mega"
    elif value>=1000:
        value = value/1000
        suffix = "kilo"

    
    result = f"{value:g} {suffix}ohms {tolerance_value[tolerance_color.index(bands[-1])]}"
    

    return result

    
