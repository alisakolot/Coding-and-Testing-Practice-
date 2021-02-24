def lemur(branches):
    """Return number of jumps needed."""

    #Tests for the code
    assert branches[0] ==  0 
    """First branch must be alive"""
    #^the index of the first branch
    assert branches[-1] ==  0 
    """Last branch must be alive"""
    #^the index of the last branch 

    br_list = [0, 0, 1, 0, 1, 0]
    nlist = []
    for branch in br_list:
        if branch == 0:
            nlist.append(branch)

    return len(nlist-1)

    #Solution specific to given 

    




    
        
        #wtf is assert? 
            #It lets you test if a condition in your code
            # returns True, if not, the program raises an 
            # assertion error

            #remember == is an building block of an expression 
            # that indicates a boolean
