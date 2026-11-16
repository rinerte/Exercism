def convert(input_grid):
    if len(input_grid)%4!=0:
        raise ValueError("Number of input lines is not a multiple of four")
    for line in input_grid:
        if len(line)%3!=0:
            raise ValueError("Number of input columns is not a multiple of three")

    numbers = [
        " _ | ||_|   ",
        "     |  |   ",
        " _  _||_    ",
        " _  _| _|   ",
        "   |_|  |   ",
        " _ |_  _|   ",
        " _ |_ |_|   ",
        " _   |  |   ",
        " _ |_||_|   ",
        " _ |_| _|   "
    ]
    result = ""
    
    for line_index in range(0,len(input_grid),4):
        for char_index in range(0,len(input_grid[line_index]),3):
            one_part = input_grid[line_index][char_index:char_index+3]
            one_part+= input_grid[line_index+1][char_index:char_index+3]
            one_part+= input_grid[line_index+2][char_index:char_index+3]
            one_part+= input_grid[line_index+3][char_index:char_index+3]            
            try:
                number = numbers.index(one_part)
                result = result+str(number)
            except:
                result = result+"?"
            
        result = result+","

    return result.strip(",")

