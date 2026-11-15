def rows(letter):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter_index = alpha.index(letter.strip())

    if letter_index==0:
        return ["A"]

    width = letter_index*2+1

    result = "A".center(width)

    for index, char in enumerate(alpha[1:letter_index+1]):
        result+="\n"
        result = result + (char + ' '*((index+1)*2-1) + char).center(width)

    lines = result.splitlines()
    
    return lines+lines[-2::-1]
    