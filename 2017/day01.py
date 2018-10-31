captcha = input()
captcha_len = len(captcha)
sum_1 = 0

for i in range(captcha_len - 1):
    if captcha[i] == captcha[i + 1]:
        sum_1 += int(captcha[i])

if captcha[0] == captcha[captcha_len - 1]:
    sum_1 += int(captcha[0])

print(sum_1)

first_part = captcha[:captcha_len / 2]
second_part = captcha[captcha_len / 2:]

sum_2 = 0

for i in range(len(first_part)):
    if first_part[i] == second_part[i]:
        sum_2 += int(captcha[i]) * 2

print(sum_2)
