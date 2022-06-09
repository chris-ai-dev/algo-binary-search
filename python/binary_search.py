def binary_search(number_to_search, list_values, iterations_right=0):
    mid_point = len(list_values)//2
    mid_value = list_values[mid_point]
    print(mid_value)
    print(list_values)
    if len(list_values) <= 1:
        return -1
    if number_to_search == mid_value:
        print(mid_value, iterations_right)
        return mid_point + iterations_right
    if number_to_search > mid_value:
        # print(mid_value)
        #need the tail end of list
        iterations_right += mid_point
        list_values = list_values[mid_point:]
    else:
        #left end
        # print(mid_value)
        list_values = list_values[:mid_point]
    print(list_values)    
    return binary_search(number_to_search, list_values, iterations_right)
    
    
print(binary_search(0,[1,2,7,8]))
"""
    1,2,3,4,5
    mid =3
    i+
    3,4,5
    mid = 4
"""