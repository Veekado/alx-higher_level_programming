#!/usr/bin/python3
#This code i commented out works fine too
#def number_keys(a_dictionary):
#    return (len(a_dictionary))

def number_keys(a_dictionary):
    count = 0
    for k, v in a_dictionary.items():
        count += 1

    return count
