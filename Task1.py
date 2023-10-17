def count_of_unique_words(file):
    with open(file, 'r') as file:
        word_occurrence= {}
        for line in file:
            words = line.split()
            for word in words:
                word = word.strip('.,!?()[]{}"\'').lower()
                if word not in word_occurrence:
                    word_occurrence[word] = 1
                else:
                    word_occurrence[word] += 1
        for word, count in word_occurrence.items():
            if count == 1:
                print(f'{word}: occurred {count} time')


# Main function
if __name__ == "__main__":
    filename = "sample.txt"
    count_of_unique_words(filename)
