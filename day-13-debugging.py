def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item) # this was not in the for loop vstudio has debugger mode for harder bugs
    print(b_list)

mutate([1,2,3,5,8,13])

# tips for debugging
#     take a break
#     ask someone
#     run code often
#     stack overflow