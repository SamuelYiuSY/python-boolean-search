import main
import time

boolean_search = main.boolean_search

one_hundred_animals_string = "Lion Tiger Bear Wolf dog rabbit Fox Squirrel cat Mouse Horse Cow Sheep Duck Goose Chicken Pig Chicken Lizard Snake Frog Turtle Bird Monkey Elephant Zebra Camel Gorilla Panda Koala Flamingo Hippo Shark Camelopardus Hamster Penguin Koala Bear Lion Leopard Cheetah Tiger Gorilla Gorilla Giraffe Elephant Rhino Orangutan Monkey Lion Tiger Eagle Wolf Bear Fox Deer Sheep Horse Cow Pig Chicken Duck Goose Rabbit Sheep Cow Horse Dog Wolf Lion Tiger Bear Fox Rabbit Cat Wolf Bear Fox Squirrel Dog Mouse Horse Cow Sheep Duck Goose Chicken Pig Lizard Snake Frog Turtle Bird Monkey Elephant Zebra Camel Gorilla Panda Koala Flamingo Hippo Shark Camelopardus Hamster Penguin Koala Bear Lion Leopard Cheetah Tiger Gorilla Gorilla Giraffe Elephant Rhino Orangutan Monkey Lion Tiger Eagle Wolf Bear Fox Deer Sheep Horse Cow Pig Chicken Duck Goose Rabbit Sheep Cow Horse Dog Wolf Lion Tiger Bear Fox Rabbit Cat Wolf Bear Fox Squirrel Dog Mouse Horse Cow Sheep Duck Goose Chicken Pig Lizard Snake Frog Turtle Bird Monkey Elephant Zebra Camel Gorilla Panda Koala Flamingo Hippo Shark Camelopardus Hamster Penguin Koala Bear Lion Leopard Cheetah Tiger Gorilla Gorilla Giraffe Elephant Rhino Orangutan Monkey Lion Tiger Eagle Wolf Bear Fox Deer Sheep Horse Cow Pig Chicken Duck Goose Rabbit Sheep Cow Horse Dog Wolf Lion Tiger Bear Fox Rabbit Cat Wolf Bear Fox Squirrel Dog Mouse Horse Cow Sheep Duck Goose Chicken Pig Lizard Snake Frog Turtle Bird Monkey Elephant Zebra Camel Gorilla Panda Koala Flamingo Hippo Shark Camelopardus Hamster Penguin Koala Bear Lion Leopard Cheetah Tiger Gorilla Gorilla Giraffe Elephant Rhino Orangutan Monkey Lion Tiger Eagle Wolf Bear Fox Deer Sheep Horse Cow Pig Chicken Duck Goose Rabbit Sheep Cow Horse Dog Wolf Lion Tiger Bear Fox Rabbit Cat Wolf Bear Fox Squirrel Dog Mouse Horse Cow Sheep Duck Goose Chicken Pig Lizard Snake Frog Turtle Bird Monkey Elephant Zebra Camel Gorilla Panda Koala Flamingo Hippo Shark Camelopardus Hamster Penguin Koala Bear Lion Leopard Cheetah Tiger Gorilla Gorilla Giraffe Elephant Rhino Orangutan Monkey Lion Tiger Eagle Wolf Bear Fox Deer Sheep Horse Cow Pig Chicken Duck Goose Rabbit Sheep Cow Horse Dog Wolf Lion Tiger Bear Fox Rabbit Cat Wolf Bear Fox Squirrel Dog Mouse Horse Cow Sheep Duck Goose Chicken Pig Lizard Snake Frog Turtle Bird Monkey Elephant Zebra Camel Gorilla Panda Koala Flamingo Hippo Shark Camelopardus Hamster Penguin Koala Bear Lion Leopard Cheetah Tiger Gorilla Gorilla Giraffe Elephant Rhino Orangutan Monkey Lion Tiger Eagle Wolf Bear Fox Deer Sheep Horse Cow Pig Chicken Duck Goose Rabbit Sheep Cow Horse Dog Wolf Lion Tiger Bear Fox Rabbit Cat Wolf Bear Fox Squirrel Dog Mouse Horse Cow Sheep Duck Goose Chicken Pig Lizard Snake Frog Turtle Bird Monkey Elephant Zebra Camel Gorilla Panda Koala Flamingo Hippo Shark Camelopardus Hamster Penguin Koala Bear Lion Leopard Cheetah Tiger Gorilla Gorilla Giraffe Elephant Rhino Orangutan Monkey Lion Tiger Eagle Wolf Bear Fox Deer Sheep Horse Cow Pig Chicken Duck Goose Rabbit Sheep Cow Horse Dog Wolf Lion Tiger Bear Fox Rabbit Cat Wolf Bear Fox Squirrel Dog Mouse Horse Cow Sheep Duck Goose Chicken Pig Lizard Snake Frog Turtle Bird Monkey Elephant Zebra Camel Gorilla Panda Koala Flamingo Hippo Shark Camelopardus Hamster Penguin Koala Bear Lion Leopard Cheetah Tiger Gorilla Gorilla Giraffe Elephant Rhino Orangutan Monkey Lion Tiger Eagle Wolf Bear Fox Deer Sheep Horse Cow Pig Chicken Duck Goose Rabbit Sheep Cow Horse Dog Wolf Lion Tiger Bear Fox Rabbit Cat Wolf Bear Fox Squirrel Dog Mouse Horse Cow Sheep Duck Goose Chicken Pig Lizard Snake Frog Turtle Bird Monkey Elephant Zebra Camel Gorilla Panda Koala Flamingo Hippo Shark Camelopardus Hamster Penguin Koala Bear Lion Leopard Cheetah Tiger Gorilla Gorilla Giraffe Elephant Rhino Orangutan Monkey Lion Tiger Eagle Wolf Bear Fox Deer Sheep Horse Cow Pig Chicken Duck Goose Rabbit Sheep Cow Horse Dog Wolf Lion Tiger Bear Fox Rabbit Cat Wolf Bear Fox Squirrel Dog Mouse Horse Cow Sheep Duck Goose Chicken Pig Lizard Snake Frog Turtle Bird Monkey Elephant Zebra Camel Gorilla Panda Koala Flamingo Hippo Shark Camelopardus Hamster Penguin Koala Bear Lion Leopard Cheetah Tiger Gorilla Gorilla Giraffe Elephant Rhino Orangutan Monkey Lion Tiger Eagle Wolf Bear Fox Deer Sheep Horse Cow Pig Chicken Duck Goose Rabbit Sheep Cow Horse Dog Wolf Lion Tiger Bear Fox Rabbit Cat Wolf Bear Fox Squirrel Dog Mouse Horse Cow Sheep Duck Goose Chicken Pig Lizard Snake Frog Turtle Bird Monkey Elephant Zebra Camel Gorilla Panda Koala Flamingo Hippo Shark Camelopardus Hamster Penguin Koala Bear Lion Leopard Cheetah Tiger Gorilla Gorilla Giraffe Elephant Rhino Orangutan Monkey Lion Tiger Eagle Wolf Bear Fox Deer Sheep Horse Cow Pig Chicken Duck Goose Rabbit Sheep Cow Horse Dog Wolf Lion Tiger Bear Fox Rabbit Cat Wolf Bear Fox Squirrel Dog Mouse Horse Cow Sheep Duck Goose Chicken Pig Lizard Snake Frog Turtle Bird Monkey Elephant Zebra Camel Gorilla Panda Koala Flamingo Hippo Shark Camelopardus Hamster Penguin Koala Bear Lion Leopard Cheetah Tiger Gorilla Gorilla Giraffe Elephant Rhino Orangutan Monkey Lion Tiger Eagle Wolf Bear Fox Deer Sheep Horse Cow Pig Chicken Duck Goose Rabbit Sheep Cow Horse Dog Wolf Lion Tiger Bear Fox Rabbit Cat Wolf Bear Fox Squirrel Dog Mouse Horse Cow Sheep Duck Goose Chicken Pig Lizard Snake Frog Turtle Bird Monkey Elephant Zebra Camel Gorilla Panda Koala Flamingo Hippo Shark Camelopardus Hamster Penguin Koala Bear Lion Leopard Cheetah Tiger Gorilla Gorilla Giraffe Elephant Rhino Orangutan Monkey Lion Tiger Eagle Wolf Bear Fox Deer Sheep Horse Cow Pig Chicken Duck Goose Rabbit Sheep Cow Horse Dog Wolf Lion Tiger Bear Fox Rabbit Cat Wolf Bear Fox Squirrel Dog Mouse Horse Cow Sheep Duck Goose Chicken Pig Lizard Snake Frog Turtle Turtle Turtle Turtle Turtle Turtle Turtle Turtle Turtle Turtle Turtle Turtle Turtle Turtle Turtle Turtle Turtle Turtle Turtle Turtle Turtle Turtle Turtle Turtle Turtle Turtle Turtle Turtle Turtle Turtle Turtle"

def test_basic_and_cases(search_whole_words_only = False):
    assert boolean_search("cat dog rabbit", AND_list=["cat", "rabbit"], search_whole_words_only=search_whole_words_only) == True
    assert boolean_search(one_hundred_animals_string, AND_list=["cat", "rabbit"], search_whole_words_only=search_whole_words_only) == True
    assert boolean_search("dog mouse", AND_list=["cat", "rabbit"], search_whole_words_only=search_whole_words_only) == False
    assert boolean_search(one_hundred_animals_string, AND_list=["non_existent_word", "rabbit"], search_whole_words_only=search_whole_words_only) == False


def test_or_only_cases(search_whole_words_only = False):
    assert boolean_search("dog mouse", OR_list=["mouse", "cat"], search_whole_words_only=search_whole_words_only) == True
    assert boolean_search(one_hundred_animals_string, OR_list=["cat", "non_existent_word"], search_whole_words_only=search_whole_words_only) == True
    assert boolean_search("dog mouse", OR_list=["elephant", "giraffe"], search_whole_words_only=search_whole_words_only) == False
    assert boolean_search(one_hundred_animals_string, OR_list=["non_existent_word", "non_existent_word_1"], search_whole_words_only=search_whole_words_only) == False
    assert boolean_search("lizard snake", OR_list=["snake"], search_whole_words_only=search_whole_words_only) == True
    assert boolean_search("lizard snake", OR_list=["rabbit"]) == False

def test_not_only_cases(search_whole_words_only = False):
    assert boolean_search("dog mouse", NOT_list=["mouse"], search_whole_words_only=search_whole_words_only) == False
    assert boolean_search(one_hundred_animals_string, NOT_list=["cat"], search_whole_words_only=search_whole_words_only) == False
    assert boolean_search("dog mouse", NOT_list=["cat"], search_whole_words_only=search_whole_words_only) == True
    assert boolean_search(one_hundred_animals_string, NOT_list=["non_existent_word"], search_whole_words_only=search_whole_words_only) == True

def test_and_or_combinations(search_whole_words_only = False):
    # AND and OR both match
    assert boolean_search("dog rabbit", ["dog"], ["rabbit"]) == True
    assert boolean_search(one_hundred_animals_string, ["dog"], ["rabbit"]) == True
    # AND matches but OR fails
    assert boolean_search("dog cat", ["dog", "cat"], ["mouse", "rabbit"]) == False
    assert boolean_search(one_hundred_animals_string, ["dog", "cat"], ["non_existent_word", "non_existent_word_1"]) == False
    # OR matches but AND fails
    assert boolean_search("dog mouse", ["rabbit", "dog"], ["mouse"], []) == False
    assert boolean_search(one_hundred_animals_string, ["non_existent_word", "dog"], ["cat"], []) == False

#TODO add one_hundred_animals_string test starting from below
def test_and_or_not_combinations(search_whole_words_only = False):
    # All and OR match, NOT passes
    assert boolean_search("dog rabbit", ["dog"], ["rabbit"], ["cat"]) == True
    # AND and OR match, NOT fails
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


def test_no_filters_returns_true(search_whole_words_only = False):
    assert boolean_search("any text here", search_whole_words_only=search_whole_words_only) == True
    assert boolean_search(one_hundred_animals_string, search_whole_words_only=search_whole_words_only) == True

def test_examples_from_prompt(search_whole_words_only = False):
    assert boolean_search("cat dog rabbit", ["cat", "rabbit"], search_whole_words_only=search_whole_words_only) == True
    assert boolean_search("dog mouse", ["cat", "rabbit"], search_whole_words_only=search_whole_words_only) == False

start_time = time.time()

test_basic_and_cases()
test_or_only_cases()
test_not_only_cases()
test_and_or_combinations()
test_and_or_not_combinations()
test_no_filters_returns_true()
test_examples_from_prompt()

end_time = time.time()

print(f"all substring tests passed in {end_time - start_time:.6f} seconds")

start_time = time.time()

test_basic_and_cases(search_whole_words_only = True)
test_or_only_cases(search_whole_words_only = True)
test_not_only_cases(search_whole_words_only = True)
test_and_or_combinations(search_whole_words_only = True)
test_and_or_not_combinations(search_whole_words_only = True)
test_no_filters_returns_true(search_whole_words_only = True)
test_examples_from_prompt(search_whole_words_only = True)

end_time = time.time()

print(f"all whole word tests passed in {end_time - start_time:.6f} seconds")
