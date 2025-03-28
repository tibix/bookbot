import sys
from stats import count_words


def count_letters(text):
    letters_count = {}
    for letter in text:
        letter = letter.lower()
        if letter.isalpha():
            if letter in letters_count:
                letters_count[letter] += 1
            else:
                letters_count[letter] = 1
    return letters_count


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []
    for ch in chars_dict:
        sorted_list.append({"char": ch, "num": chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = sys.argv[1]

    with open(book) as f:
        file_contents = f.read()
    print(f"--- Begin report of {book} ---")
    print(f"{count_words(file_contents)} words found in the document\n")

    counted_letters = count_letters(file_contents)
    chars_sorted_list = chars_dict_to_sorted_list(counted_letters)

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"- '{item['char']}: {item['num']}'")

    print("--- End report ---")


if __name__ == "__main__":
    main()
