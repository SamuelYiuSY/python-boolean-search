import main

boolean_search = main.boolean_search


def test_basic_and_cases():
    assert boolean_search("cat dog rabbit", ["cat", "rabbit"]) == True
    assert boolean_search("dog mouse", ["cat", "rabbit"]) == False

def test_or_only_cases():
    assert boolean_search("dog mouse", [], ["mouse", "cat"]) == True
    assert boolean_search("dog mouse", [], ["elephant", "giraffe"]) == False
    assert boolean_search("lizard snake", [], ["snake"], []) == True
    assert boolean_search("lizard snake", [], ["rabbit"], []) == False

def test_not_only_cases():
    assert boolean_search("dog mouse", [], [], ["mouse"]) == False
    assert boolean_search("dog mouse", [], [], ["cat"]) == True
    
def test_and_or_combinations():
    # AND and OR both match
    assert boolean_search("dog rabbit", ["dog"], ["rabbit"]) == True
    # AND matches but OR fails
    assert boolean_search("dog cat", ["dog"], ["mouse", "rabbit"]) == False
    # OR matches but AND fails
    assert boolean_search("dog mouse", ["rabbit"], ["mouse"], []) == False
    # OR matches but AND fails, explicit
    assert boolean_search("mouse elephant", ["dog"], ["mouse"], []) == False
    # AND matches, no OR list
    assert boolean_search("dog rabbit", ["dog"], [], []) == True
    # OR matches, no AND list
    assert boolean_search("dog rabbit", [], ["rabbit"], []) == True


def test_and_or_not_combinations():
    # All match, NOT passes
    assert boolean_search("dog rabbit", ["dog"], ["rabbit"], ["cat"]) == True
    # AND and OR match, but NOT excludes
    assert boolean_search("dog rabbit cat", ["dog"], ["rabbit"], ["cat"]) == False
    # AND matches, OR fails, NOT passes
    assert boolean_search("dog rabbit", ["dog"], ["mouse"], ["cat"]) == False
    # AND fails, OR matches, NOT passes
    assert boolean_search("dog rabbit", ["elephant"], ["rabbit"], ["cat"]) == False
    # AND matches, OR matches, NOT fails
    assert boolean_search("dog rabbit cat", ["dog"], ["rabbit"], ["cat"]) == False
    # AND matches, OR fails, NOT fails
    assert boolean_search("dog cat", ["dog"], ["mouse"], ["cat"]) == False
    # AND fails, OR matches, NOT fails
    assert boolean_search("rabbit cat", ["dog"], ["rabbit"], ["cat"]) == False
    # AND fails, OR fails, NOT passes
    assert boolean_search("dog rabbit", ["elephant"], ["mouse"], ["cat"]) == False


def test_no_filters_returns_true():
    assert boolean_search("any text here", [], [], []) == True


def test_examples_from_prompt():
    assert boolean_search("cat dog rabbit", ["cat", "rabbit"]) == True
    assert boolean_search("dog mouse", ["cat", "rabbit"]) == False

test_basic_and_cases()
test_or_only_cases()
test_not_only_cases()
test_and_or_combinations()
test_and_or_not_combinations()
test_no_filters_returns_true()
test_examples_from_prompt()
