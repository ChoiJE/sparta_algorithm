input = 20

# 소수는 자기 자신과 1외 에는 아무것도 나눌 수 없다.
# 주어진 자연수 N이 소수이기 위한 필요 충분 조건은
# N이 N의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는다.
# 수가 수를 나누면 몫이 발생하는데, 몫과 나누는 수 둘 중 하나는
# 반드시 N 제곱근 이하이다.
def find_prime_list_under_number(number):
    count = 0
    primary_num_array = []

    for num in range(2, number + 1): # 2 ~ number 까지의 숫자
        for i in primary_num_array:
            if num % i == 0 and i * i <= num:
                break

        else:
            primary_num_array.append(num)

    return primary_num_array


result = find_prime_list_under_number(input)
print(result)