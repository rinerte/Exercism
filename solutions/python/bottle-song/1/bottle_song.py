def recite(start, take=1):
    numbers = [
        "Ten",
        "Nine",
        "Eight",
        "Seven",
        "Six",
        "Five",
        "Four",
        "Three",
        "Two",
        "One",
        "No"
    ]
    list = []
    s = "s"
    ss = "s"
    for repeat in range(start,start-take,-1):        
        if repeat==1:
            s = ""
        else:
            s="s"
        if repeat==2:
            ss = ""
        else:
            ss="s"
        list.append(f"{numbers[-(repeat+1)]} green bottle{s} hanging on the wall,")
        list.append(f"{numbers[-(repeat+1)]} green bottle{s} hanging on the wall,")
        list.append("And if one green bottle should accidentally fall,")
        list.append(f"There'll be {str(numbers[-repeat]).lower()} green bottle{ss} hanging on the wall.")
        if repeat-1>start-take:
            list.append("")

    return list
