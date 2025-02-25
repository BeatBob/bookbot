# books/frankenstein.txt
def get_num_words(path):
    with open(path) as f:
        file_contents = f.read()
        file_word_count = file_contents.split()
        word_length = len(file_word_count)
        character_count(file_contents.lower(),word_length)
        # print(f"{word_length} words found in the document")

def character_count(file_content,word_length):
    every_character = list(file_content)
    each_character_exist = set(every_character)
    each_character_exist_dict = {}
    for character in each_character_exist:
        each_character_exist_dict[character] = 0
    for char in every_character:
        if char in each_character_exist_dict:
            each_character_exist_dict[char] += 1

    summary(word_length, each_character_exist_dict)



def summary(word_length, each_character_exist_dict):
    char_list_tuples = list(each_character_exist_dict.items())
    temp_list = []
    for tuples in char_list_tuples:
        temp_list.append({tuples[0]:tuples[1]})

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_length} total words")
    print("----------- Character Count ----------")
    temp_list.sort(reverse=True, key=lambda x: list(x.values())[0])
    for dict in temp_list:
        first_key = next(iter(dict))  # Get the first key dynamically
        for item in dict:
            if item.isalpha():
                print(f"{first_key}: {dict[first_key]}")
    print("============= END ===============")



