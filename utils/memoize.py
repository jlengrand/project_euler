#!/usr/bin/env python 
'''
Created on 17 feb. 2012

@author: Julien Lengrand-Lambert
@contact: julien@lengrand.fr
''' 

def memoize(function):
    """Defines a memoization scheme"""
    cache = {}
    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            val = function(*args)
            cache[args] = val
            return val
    return decorated_function