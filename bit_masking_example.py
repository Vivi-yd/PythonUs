# this is an section of codes from a project where bit-masking is being used"

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.
    hand: full yahtzee hand
    Returns a set of tuples, where each tuple is dice to hold
    """
    # initiate a list for all possible holds 
    all_choices_lst = []
    # define a set that represent choose/not choose (like on/off switch)
    choice = [1, 0]
    
    # generates all possible ways (will be called vectors like matrices)
    # of choosing or not choosing in a list of 3
    vectors = gen_all_sequences(choice, len(hand))
    
    
    # for each vector in vectors
    for vec in vectors:
        # interate over the each value in vector
        temp_list = []

        for idx in range(len(vec)):
 
            # if the value is 1, add the corresponding value of the index in
            # hand into the temparory set
            if vec[idx] == 1:
                temp_list.append(hand[idx])
        # then add the temp_set into the list of all possible holds        
        all_choices_lst.append(temp_list)    
    
    
    return lst_to_tup(all_choices_lst)