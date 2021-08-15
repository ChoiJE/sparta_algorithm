# 이진탐색
finding_target = 12
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# 1단계 : 최솟값 1, 최댓값 16 의 중간이 8 시도
# 2단계 : 최솟값 9, 최댓값 16 의 중간이 12 시도
# 3단계 : 최솟값 13, 최댓값 16 의 중간이 14 시도

def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array)-1
    current_guess = (current_min + current_max) // 2

    while current_min <= current_max:
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_min + current_max) // 2
    return False

    # 구현해보세요!
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)