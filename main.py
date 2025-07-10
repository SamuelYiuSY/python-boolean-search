def boolean_search(string_to_search, AND_list = None, OR_list = None, NOT_list = None):
    if AND_list:
        for eachWord in AND_list:
            if eachWord not in string_to_search:
                # print("AND statement not satisified")
                return False
    
    if OR_list:
        have_1_OR_word_flag = False
        for eachWord in OR_list:
            if eachWord in string_to_search:
                have_1_OR_word_flag = True
                break
        if not have_1_OR_word_flag:
            # print("OR statement not satisified")
            return False
    
    if NOT_list:
        for eachWord in NOT_list:
            if eachWord in string_to_search:
                # print("NOT statement not satisified")
                return False
    
    return True
    



