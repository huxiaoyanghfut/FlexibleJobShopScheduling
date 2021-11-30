import pandas as pd
import numpy as np
import copy
def parse_data():
    job_machine_tmp = pd.read_excel("排产输入数据样例.xlsx",sheet_name="工序可选机器表")
    processing_time_tmp = pd.read_excel("排产输入数据样例.xlsx",sheet_name="各工序加工时间")

    ptshape = processing_time_tmp.shape
    machine_number = 10
    job_number = ptshape[0]
    processing_time = []
    job_machine = []
    operation_number = []
    ## 初始化每个工件的工序数量operation_number
    for i in range(job_number):
        job_tmp = list(job_machine_tmp.iloc[i, 1:])
        print(job_tmp)
        k = 0
        while(k < len(job_tmp)):
            if job_tmp[k] == 0:
                operation_number.append(k)
                break
            k += 1
        if k == len(job_tmp):
            operation_number.append(len(job_tmp))
    print(operation_number)

    ## 初始化job_machine
    for i in range(job_number):
        job_tmp = job_machine_tmp.iloc[i, 1:]
        job = []
        for m in job_tmp:
            if isinstance(m, str):
                job.append(list(map(int, m.split(','))))
            else:
                job.append([m])
        job_machine.append(copy.deepcopy(job))
    ## 初始化processing_time

    for i in range(job_number):
        pt_tmp = processing_time_tmp.iloc[i, 1:]
        time = []
        for t in pt_tmp:
            if isinstance(t, str):
                time.append(list(map(int, t.split(','))))
            else:
                time.append([t])
        processing_time.append(copy.deepcopy(time))
    return job_machine, processing_time, machine_number, operation_number
