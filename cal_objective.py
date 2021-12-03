import copy
import math
def cal_objective(cur, machine_number, operation_number, job_machine, processing_time):
    """
        解码出最大完工时间
    """
    job_number = len(operation_number)
    total_operations = sum(operation_number)
    operation_code = cur[:total_operations]
    machine_code = cur[total_operations:2*total_operations]
    # 计算调度工序
    counter = [0 for i in range(job_number)]
    operation = [0 for i in range(total_operations)]
    for i in range(len(operation_code)):
        counter[operation_code[i]-1] = counter[operation_code[i]-1] + 1
        operation[i] = operation_code[i]*100 + counter[operation_code[i]-1]
    # 计算机器时间和工序时间
    operation_time = [[0 for col in range(total_operations)] for row in range(2)]
    machine_available_time = [0 for i in range(machine_number)]
    operation_available_time = [0 for i in range(job_number)]
    ## 解码机器部分machine_code得到工序加工机器矩阵job_machine_fix和processing_time_fix
    job_machine_fix = [[0 for col in range(max(operation_number))] for row in range(job_number)]
    processing_time_fix = [[0 for col in range(max(operation_number))] for row in range(job_number)]
    count = 0
    for i in range(job_number):
        op_num = operation_number[i]
        for j in range(op_num):
            machines = job_machine[i][j]
            job_machine_fix[i][j] = machines[machine_code[count]]
            processing_time_fix[i][j] = processing_time[i][j][machine_code[count]]
            count += 1
    ## 解码工序部分得到各工序的开始时间和完工时间
    for i in range(total_operations):
        op = operation[i]
        op_index = op % 100
        job_index = math.floor((op - op_index)/100)
        mc = job_machine_fix[job_index-1][op_index-1]
        pt = processing_time_fix[job_index-1][op_index-1]
        pre_op_cpt = operation_available_time[job_index-1]
        cur_machine_time = machine_available_time[mc-1]
        op_start_time = max(pre_op_cpt, cur_machine_time)
        operation_time[0][i] = op_start_time
        operation_time[1][i] = op_start_time + pt
        operation_available_time[job_index-1] = operation_time[1][i]
        machine_available_time[mc-1] = operation_time[1][i] 
    # 取最大完工时间
    completion_max_time = operation_time[1][0]
    for i in range(total_operations):
        if operation_time[1][i] > completion_max_time:
            completion_max_time = operation_time[1][i]
    return completion_max_time