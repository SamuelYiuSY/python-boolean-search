def boolean_search(search_string, AND_list = None, OR_list = None, NOT_list = None, search_whole_words_only = False):
    if search_whole_words_only == True:
        # convert string_to_search from string to set to speed up
        search_string = set(search_string.split())
    
    # check OR and NOT list first as they may return before going through the whole string
    if OR_list:
        have_1_OR_word_flag = False
        for eachWord in OR_list:
            if eachWord in search_string:
                have_1_OR_word_flag = True
                break
        if not have_1_OR_word_flag:
            # print("OR statement not satisified")
            return False
    
    if NOT_list:
        for eachWord in NOT_list:
            if eachWord in search_string:
                # print("NOT statement not satisified")
                return False

    if AND_list:
        for eachWord in AND_list:
            if eachWord not in search_string:
                # print("AND statement not satisified")
                return False
    
    return True
    



