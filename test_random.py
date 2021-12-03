import random
from initialization import initialization
# choices = [1,2,3]
# for i in range(100):
#     choice = random.choice(choices)
#     print(choice)

# test1 = choices[:3]
# print(test1)
# operation_number = [4, 7, 7, 7, 7, 7, 7, 7, 7, 7]
# job_machine = [[[1], [2, 4], [3], [4, 8], [0], [0], [0]], [[1], [3], [5], [10], [4], [2], [7]], [[2], [1, 10], [4], [3], [9], [6], [8]], [[2], [3], [1], [5], [7], [9], [8]], [[3], [1], [2, 7], [6], [4], [5], [9]], [[3, 8], [2], [6], [4], [9], [10], [1]], [[2], [1], [4], [3, 5], [7], [6], [10]], [[3], [1], [2], [6], [5], [7], [9]], [[1], [2], [4, 5], [6], [3], [10, 3], [7]], [[2], [1, 8], [3], [7], [9], [10], [6]]]
# cur = initialization(operation_number, job_machine)
# print(cur)
# print(operation_number[:3])
# a = ['9']
# print(len(a))
list4seclet = [i for i in range(50)]
positions = random.sample(list4seclet, 2)
print(positions)