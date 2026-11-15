def commands(binary_str):
    actions = ["jump","close your eyes","double blink","wink"]

    set = []

    for i in range(len(binary_str) - 1, 0, -1):
        if binary_str[i]=="1":
            set.append(actions[i-1])

    if binary_str[0]=="1":
        set.reverse()

    return set
    
