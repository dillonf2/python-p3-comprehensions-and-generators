#!/usr/bin/env python3

def return_evens(num_list):
    updated_list=[]
    for num in num_list:
        if float(num/2)==int(num/2):
            updated_list.append(num)
    return updated_list
            
def make_exclamation(sentence_list):
    new_string_list=[]
    for string in sentence_list:
        new_string_list.append(string+"!")
    return new_string_list

