"""
    This file contains your final_strategy that will be submitted to the contest.

    You can only depend on "general-purpose" libraries - do not import or open any
    contest-specific files, like other Python or text files. All contest logic must
    be in this file.

    Remember to supply a unique PLAYER_NAME or your submission will not succeed.
""" 

PLAYER_NAME = 'Catxxxl'  # Change this line!


def final_strategy(s, o):
    if s>51 or o >51:
        return 0
    return bn(s, o)
def m(f):
    d = {}
    def lp(*args):
        k = (f, args)
        if not k in d:
            d[k] = f(*args)
        return d[k]
    return lp
@m
def bn(s, o):
    bp, b = 0, 1
    for n in range(0, 10 + 1):
        p = po(s, o, n)
        if p > bp:
            bp, b = p, n
    return b
@m
def po(s, o, n):
    pow=0
    if n == 0:
        s1 = pp(o)
        pow = po2(s + s1, o)
    else:
        for p_s in range(1, (6 * n) + 1):
            pow += poc(p_s, n,6) * po2(s + p_s, o)
    return pow
   
@m 
def po2(s, o):
    if ss(s, o):
        s, o = o, s
    if s >= 50:
    
        return 1
    elif o >= 50:
    
        return 0
    on = 6
    poo = po(o, s, on)
    return 1 - poo
        
@m
def no(k, n, s):
    if k < 0:
        return 0
    if k == 0 and n == 0:
        return 1
    if n == 0:
        return 0
    total = 0
    for i in range(2, s + 1):
        total += no(k - i, n - 1, s)
    return total
@m
def poc(k, n, s):
    if k == 1:
        return 1-pow(s - 1, n)/pow(s, n)
    return no(k, n, s)/pow(s, n)
def ss(s, o):
    A = str(pow(3,s + o))
    if A[0] == A[len(A)-1]:
        return True
    else:
        return False 
def pp(s):
    if s == 0:
        return 1
    else:        
        w = s%6
        if w ==1:
            return 0
        if w ==2:
            return 4
        if w ==3:
            return 7
        if w ==4:
            return 6
        if w == 5:
            return 1
        else:
            return 9
