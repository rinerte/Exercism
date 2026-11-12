def is_paired(input_string):
    brackets = ["[","(","{","]",")","}"]
    stack = []

    for char in input_string:
        if char in brackets[:3]:
            stack.append(char)
        elif char in brackets[3:]:
            if len(stack)==0:
                return False
            if brackets.index(char)-3 != brackets.index(stack.pop()):
                return False  
                
    if len(stack)>0:
        return False
        
    return True
            
