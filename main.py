def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    character_dict = get_character_count(text)
    new_list = convert_dictionaries(character_dict)
    report_list = get_dictionary_values(new_list)
    get_report(report_list, book_path, num_words)

def get_report(report_list , book_path, num_words):
    print()
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for report in report_list:
        print(report)
    print("--- End report ---")
    print()

    
def get_dictionary_values(new_list):
    report_list= []
    for item in new_list:
        report = f"The '{item['char']}' character was found {item['num']} times"
        report_list.append(report)
    return report_list           



def sort_on(character_dict):
    return character_dict["num"]   

    
    
def convert_dictionaries(character_dict):
    new_list = []
    for char, num in character_dict.items():
        dictionary_list = {"char": char, "num": num}
        new_list.append(dictionary_list)
    new_list.sort(reverse=True, key=sort_on)
    
    return new_list


def get_word_count(text):
    words = text.split()
    return len(words)


def get_character_count(text):
    character_dict = {}
    lowered_text = text.lower()
    

    for character in lowered_text:
        if character.isalpha():
            if character not in character_dict:
                character_dict[character] = 1
            else:
                character_dict[character] += 1
    return character_dict


    
        

def get_book_text(path):
    with open(path) as f:
        return f.read()



       
if __name__ == "__main__":
    main()



