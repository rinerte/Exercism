def is_armstrong_number(number):
    temp = number
    digits = 0;
    while temp>0:
        temp = temp // 10
        digits+=1
        
    temp = number
    count = 0
    while temp>0:
        count+= (temp % 10) ** digits
        temp = temp // 10

    return count == number
        