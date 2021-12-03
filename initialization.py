import random
import copy
def initialization(operation_number, job_machine):
    """
        生成初始解
    """
    job_number = len(operation_number)
    total_operations = sum(operation_number)
    remain_operations_number = copy.deepcopy(operation_number) 
    cur = []
    # 工序编码部分
    for i in range(total_operations):
        job_index = random.randint(1, job_number)
        while remain_operations_number[job_index-1] == 0:
            job_index = random.randint(1, job_number)
        cur.append(job_index)
        remain_operations_number[job_index-1] -= 1
    
    # 机器编码部分
    for i in range(job_number):
        operations = operation_number[i]
        for j in range(operations):
            available_machines = job_machine[i][j]
            cur.append(random.randint(0, len(available_machines)-1))
    return cur