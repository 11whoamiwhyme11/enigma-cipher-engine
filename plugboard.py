def plugboard(x:dict , y : str):
    for k,v in x.items():
        if k==y:
            return v
    return y
