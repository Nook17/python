#!/usr/bin/env python3

def auto(model):
    print("Your favorite car model is ", model)

def suma(a, b):
    return(a + b)

def more_arg_tuple(*arg):                   # arguments like TUPLE
    print(arg)

def more_arg_dictionaries(**arg):           # arguments like DICTIONARIES
    print(arg)

def more_arg_mix(a, b, c=3, *arg, **karg):  # arguments MIX
    print(a, b, c, arg, karg)