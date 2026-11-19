def encode(numbers):
    list = []
    for n in numbers:
        list.extend(encode_one(n))
    return list


def decode(bytes_):
    result = []
    current_number = 0
    in_sequence = False

    for byte in bytes_:
        current_number = (current_number << 7) | (byte & 0x7F)
        if byte & 0x80:
            in_sequence = True
        else:
            result.append(current_number)
            current_number = 0
            in_sequence = False

    if in_sequence:
        raise ValueError("incomplete sequence")

    return result

def encode_one(number):
    binary_string = f'{number:b}'
    list_of_128 = []
    list_of_128 = [binary_string[max(0, i - 7):i] for i in range(len(binary_string), 0, -7)][::-1]
    list_of_128[0] = list_of_128[0].zfill(7)
    
    if len(list_of_128) > 1:        
        for index in range(0,len(list_of_128)-1):
            list_of_128[index] = "1"+list_of_128[index]

    list_of_128 = [int(number, 2) for number in list_of_128]
        
    return list_of_128
    