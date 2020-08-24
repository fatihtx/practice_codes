def array_manip(array):
#    return_array = list()
#    for i in range(len(array)):
#        new_array = list()
##        for a in array[i+1:]:
##            if a > array[i]:
##                new_array.append(a)
#        value_to_return = min([a for a in array[i+1:] if a > array[i]],default=-1)
#        return_array.append(min([a for a in array[i+1:] if a > array[i]],default=-1))
#    return return_array
    return [min([a for a in array[i+1:] if a > array[i]],default=-1) for i in range(len(array))]
