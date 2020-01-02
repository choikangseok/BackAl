# natural_number_set = set(range(1, 1001))
# generated_number_set = set()
#
# for i in range(1, 1001):
#     print('currnet i = ' + str(i))
#     for j in str(i):
#         print('currnet j = ' + str(j))
#         i += int(j)
#     print('**managed num = ' + str(i))
#     generated_number_set.add(i)
#     print()
#
# print(generated_number_set)
# print(natural_number_set)
#
# self_numbers_set = natural_number_set - generated_number_set
# print(sorted(self_numbers_set))

from sys import stdin

natural_number_set = set(range(1, 10001))
generated_number_set = set()
for i in range(1, 10001):
    for j in str(i):
        i = i+ int(j)
    generated_number_set.add(i)

self_numbers_set = natural_number_set - generated_number_set


for item in sorted(self_numbers_set):
    print(item)
