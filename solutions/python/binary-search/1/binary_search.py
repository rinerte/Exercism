def find(search_list, value):
    left = 0
    right = len(search_list)-1
    center = 0
        
    while left<=right:   
        center = (left + right) // 2
        if search_list[center]==value:
            return center
        elif search_list[center]<value:
            left=center+1
        else:
            right=center-1
        

    raise ValueError("value not in array")
        
