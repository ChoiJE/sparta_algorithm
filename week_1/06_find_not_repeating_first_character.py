input = "abaabajde"


def find_not_repeating_character(string):
    alpha_array = [0] * 26
    # 이 부분을 채워보세요!
    for alpha in string:
        array_num = ord(alpha) - ord('a')
        alpha_array[array_num] += 1

    not_repeating_character_array = []
    for num in range(len(alpha_array)):
        if alpha_array[num] == 1:
            not_repeating_character_array.append(chr(num + ord("a")))

    for alpha in string:
        if alpha in not_repeating_character_array:
            return alpha

    return "_"


result = find_not_repeating_character(input)
print(result)
