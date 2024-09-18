# Возможно ли сделать без этой библиотеки? И есть ли методы чтобы фильтровало реальные слова?
from collections import Counter
def can_form_word(main_word, target_word):
    main_counter = Counter(main_word)
    target_counter = Counter(target_word)
    for letter in target_counter:
        if target_counter[letter] > main_counter[letter]:
            return False
    return True

def typesetter(file_name, main_word):
    main_word = main_word.lower()
    with open(file_name, 'r', encoding='utf-8') as f:
        words = f.read().splitlines()
    valid_words = [word for word in words if can_form_word(main_word, word)]
    for word in valid_words:
        print(word)
    print(f"\nСколько слов удалось найти? {len(valid_words)}")

file_name = 'words-list-russian.txt'
source_word = 'лекарство'
typesetter(file_name, source_word)
