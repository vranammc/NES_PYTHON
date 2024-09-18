def word_count(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
    with open(file_name, 'rb') as f:
        num_bytes = len(f.read())
    return (num_lines, num_words, num_bytes)

file_name = 'words-list-russian.txt'
result = word_count(file_name)
print(result)
