def score(h):
    p=na=0 #point is 0, number of Ace
    for i in h:
        if i=='J' or i=='Q' or i=='K':
            p+=10
        elif i=='A':
            na+=1
        else:
            p+=int(i)
    if na:
        if p+11+na-1>21: #if one Ace is counted as 11
            p+=na
        else:
            p+11+na-1
    if p>21: p=0
    return p
print(score(['2', 'A', 'A', '6']))