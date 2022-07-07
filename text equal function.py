# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 14:43:09 2022

@author: n1638
"""
import numpy as np
import re


def string_replace(string, replacements):
    """
    Utility function executes regex replacements on `string`
    Replacements is a list of lists of lists of strings (n x 2 x m_n)):
        [[ 'replacement 1', ['pattern 1', 'pattern 2'...] ],
         [ 'replacement 2', ['pattern 1', 'pattern 2'...] ],
         ... ]
        n -> number of characters
        m_n -> number of possible replacements per character n
    """
    for change in replacements:
        for alternative in change[1]:
            string = re.sub(alternative, change[0][0], string)
    return string

def grading_function(body: dict) -> dict:
    """
    Function used to grade a student response.
    """

    # Get the response and answer (use try/except..)
    res = np.array(body["response"], dtype=str)
    ans = np.array(body["answer"], dtype=str)

    
    # Get replacement list
    replacements = []

    # Change the string
    ans = string_replace(ans, replacements)
    
    # Check if ans is symbolic equal to res
    is_correct = (ans==res)

    return {"is_correct": is_correct}


# main
replacements = [['c', ['constant', 'const', 'C', 'CONSTANT']], ['x', ['X']], ['y', ['Y']]]
string = 'X**2 + 3y + const'

print(string_replace(string, replacements))