def check(strcheck:str,checks:str) :
    #eg. a = 'fe'
    #check (a,fe)
    #return is none
    if strcheck in checks :
        return'in'
    if strcheck == checks :
        return'False'
    if strcheck != checks :
        return 'False'
def replaces(how:str,what,which):
    count = 0
    for i in len(how) :
        if how[i] == what:
            run = run + 1
        if run == which:
            how[i]=what
            return how