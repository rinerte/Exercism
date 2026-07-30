def translate(text):
    return " ".join(pig(word) for word in text.split())

def pig(word, index=0):
    start = {'a', 'e', 'i', 'o', 'u', 'xr', 'yt'}
    
    if word.startswith(tuple(start)) or (word.startswith("y") and index>0):
        return word+"ay"
    elif word.startswith(("qu")):
        return word[2:]+"quay"        
    return pig(word[1:]+word[0],index+1)