punctuation_marks = {"-", ",", ".", "!", "?", "'"}
with open('text.txt') as f:
    count = 0
    for line in f:
        count += 1
        letters = 0
        punctuation_count = 0
        for i in range(len(line)):
            if line[i] in punctuation_marks:
                punctuation_count += 1
            elif line[i].isalpha():
                letters += 1

        print(f'Line {count}: {line} ({letters})({punctuation_count})')
