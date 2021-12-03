import random
import copy
def neighboring_cur(cur, job_machine, operation_number):
    """
    生成cur的邻域解
    1.随机选择一个工序，重新分配加工机器
    2.在operation_code中随机选择两个位置交换编码
    """
    total_operations = sum(operation_number)
    job_number = len(operation_number)
    operation_code = cur[:total_operations]
    machine_code = cur[total_operations:2*total_operations]
    next = []
    # 1.随机选择一个工序，重新分配加工机器
    mutation_index = random.randint(0, total_operations-1)
    child_machine_code = copy.deepcopy(machine_code)
    count = 0
    for i in range(job_number):
        op_num = operation_number[i]
        for j in range(op_num):
            if count == mutation_index:
                machines =job_machine[i][j]
                child_machine_code[count] = random.randint(0, len(machines)-1)
            count += 1
    # 2.在operation_code中随机选择两个位置交换编码
    child_operation_code = copy.deepcopy(operation_code)
    list4seclet = [i for i in range(total_operations)]
    positions = random.sample(list4seclet, 2)
    pos1 = positions[0]
    pos2 = positions[1]
    code_tmp = child_operation_code[pos1]
    child_operation_code[pos1] = child_operation_code[pos2]
    child_operation_code[pos2] = code_tmp
    next = copy.deepcopy(child_operation_code)
    next += child_machine_code
    return next