#!/usr/bin/env python

# word = "gLfc YKFFWRP )eh(( BJWYh)xQBfGn"

def duplicate_encode(word):
    mtlist = []
    ytword = word.replace(' ', '')
    for lt in word:
        x = ytword.lower().count(lt)
        # print(x)
        if x <= 1:
            mtlist.append('(')
        else:
            mtlist.append(')')
    
    corlst = ''.join(mtlist)
    print(corlst)
    return ''.join(mtlist)

duplicate_encode(')))(()())())')

"""
'())())))(()()))())))' should equal '())())))(()(())(())(
())())))(()()))())))(()
"""