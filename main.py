# Task_1 Comparing two tuples

melody = ('17', '00012456', 'Tashkent')
veritas = ('19', '00015786', 'Canada')

greater = melody > veritas
greater_equal = melody >= veritas
less_equal = melody <= veritas
equal = melody == veritas
not_equal = melody != veritas

print(f'Result is equal: {greater}')
print(f'Result is equal: {greater_equal}')
print(f'Result is equal: {less_equal}')
print(f'Result is equal: {equal}')
print(f'Result is equal: {not_equal}')


# Task_2 (advance)
def get_longest_word(list_of_words):
    named_list_of_word = input(('', ''))
    print(f'The long word in list is {max(named_list_of_word)} and {len(named_list_of_word)}')

# get_longest_word()
