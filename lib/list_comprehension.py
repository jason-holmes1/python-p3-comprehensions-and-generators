#!/usr/bin/env python3

def return_evens(num_list=[]):
    #! not using list comprehension
    new_set=[]
    for num in num_list:
        if num % 2 == 0:
            new_set.append(num) # This will return the first even number in the list
    return new_set
    #! using list comprehension
    #return [num for num in num_list if num % 2 == 0]


    

def make_exclamation(sentence_list=[]):
    # new_set=[]
    # for sentence in sentence_list:
    #     sentence += "!"
    #     new_set.append(sentence)
    # return new_set
    #! using list comprehension
     # This will return the first sentence with an exclamation mark
    return [sentence + "!" for sentence in sentence_list]