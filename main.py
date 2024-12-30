def characters(low):
    char = {}
    low_string = low.lower()
    for i in low_string:
        if i.isalpha() or i.isdigit():
            if i in char:
                char[i] += 1
            else:
                char[i] = 1
    return char
def diction(char_freq_dict):
    char_list = list(char_freq_dict.items())
    sorted_chars = sorted(char_list, key=lambda x: x[1], reverse=True)
    report_lines = []
    for char, freq in sorted_chars:
        report_lines.append(f"The '{char}' character was found '{freq}' times")
    return report_lines

def num_word(text):
    words = len(text.split())
    return words

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    word_count = num_word(file_contents)
    print(f"{word_count} words are in this book")
    dic_low = characters(file_contents)
    report_lines = diction(dic_low)
    for line in report_lines:
        print(line)

if __name__ == "__main__":
    main()
