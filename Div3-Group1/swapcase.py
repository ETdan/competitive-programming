def (s):
    n=""
    for a in s:
        if(a==a.lower()):
            n+=a.upper()
        else:
            n+=a.lower()
            
    return n

