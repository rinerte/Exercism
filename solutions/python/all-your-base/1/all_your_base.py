def rebase(input_base, digits, output_base):
    if input_base<2:
        raise ValueError("input base must be >= 2")
    if output_base<2:
        raise ValueError("output base must be >= 2")

    dex = 0

    for item in digits:
        if not (0 <= item < input_base):
            raise ValueError("all digits must satisfy 0 <= d < input base")
        dex = dex * input_base + item
        
    if dex==0:
        return [0]
        
    new_digits = []

    while dex>0:
        new_digits.append(dex%output_base)
        dex = dex // output_base
          
    return new_digits[::-1]
    
    
