d = [11, 2, 7, 22, 13, 42, 55] 

def bubble_sort (list):
    final_list = []
    temp_list = []
    for i in range (len(list)):
        a = list[i]
        b = list[i + 1]
        if a > b:
            a, b = b, a
            final_list.append (a)
            final_list.append (b)
            return final_list, permute == True

print (bubble_sort (d)) 