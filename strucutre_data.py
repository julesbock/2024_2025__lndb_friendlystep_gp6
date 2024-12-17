chain=[1,5,2,1,25,1,25,2,9,32,12]
def bubble_sort(chain):
    permutate = None
    while permutate != 0:
        permutate = 0
        for each_ in range(1, len(chain)):
            if chain[each_-1]>chain[each_]:
                chain[each_-1], chain[each_]= chain[each_], chain[each_-1]
                permutate += 1
    return chain
    
print(bubble_sort(chain))

            # permutation, chain = chain_modifier(chain)

# def chain_modifier(chain):
#     permutate = 0
#     for each_ in range(1, len(chain)):
#         a=chain[each_-1]
#         b=chain[each_]
#         if a>b:
#             a, b= b, a
#             permutate += 1
#             chain_modifier(chain)
#         chain[each_-1]=a
#         chain[each_]=b
#     return permutate, chain