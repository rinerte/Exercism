def is_valid(isbn):
    cleaned = isbn.replace("-", "").replace(" ", "").upper()
    
    if len(cleaned) != 10:
        return False
        
    if not cleaned[:9].isdigit():
        return False
        
    if not (cleaned[9].isdigit() or cleaned[9] == 'X'):
        return False
    
    total_sum = 0
    for i in range(10):
        if cleaned[i] == 'X':
            value = 10
        else:
            value = int(cleaned[i])
            
        total_sum += value * (10 - i)

    return total_sum % 11 == 0