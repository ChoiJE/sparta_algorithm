input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for alpha in string:
        if alpha.isalpha():
            array_num = ord(alpha)-ord('a')
            alphabet_occurrence_array[array_num] += 1

    max_num = 0
    max_num_array_count = 0

    for num in range(len(alphabet_occurrence_array)):
       if alphabet_occurrence_array[num] > max_num:
           max_num = alphabet_occurrence_array[num]
           max_num_array_count = num

    result = chr(max_num_array_count + ord('a'))

    return result


result = find_max_occurred_alphabet(input)
print(result)