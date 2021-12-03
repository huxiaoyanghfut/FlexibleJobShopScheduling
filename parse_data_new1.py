import pandas as pd
import copy
def parse_data_new1():
    job_machine_tmp = pd.read_excel("排产输入数据样例2.xlsx",sheet_name="工序可选机器表")
    processing_time_tmp = pd.read_excel("排产输入数据样例2.xlsx",sheet_name="各工序加工时间")

    ptshape = processing_time_tmp.shape
    machine_number = 6
    job_number = ptshape[0]
    processing_time = []
    job_machine = []
    operation_number = []
    ## 初始化每个工件的工序数量operation_number
    for i in range(job_number):
        job_tmp = list(job_machine_tmp.iloc[i, 1:])
        k = 0
        while(k < len(job_tmp)):
            if job_tmp[k] == 0:
                operation_number.append(k)
                break
            k += 1
        if k == len(job_tmp):
            operation_number.append(len(job_tmp))

    ## 初始化job_machine
    for i in range(job_number):
        job_tmp = job_machine_tmp.iloc[i, 1:]
        job = []
        for m in job_tmp:
            if isinstance(m, str):
                if m is '[]':
                    job.append([0])
                else:
                    m_tmp = m.strip('[]').split(',')
                    print(m_tmp)
                    job.append(list(map(int, m_tmp)))
            else:
                job.append([m])
        job_machine.append(copy.deepcopy(job))
    print(job_machine)
    
    ## 初始化processing_time
    for i in range(job_number):
        pt_tmp = processing_time_tmp.iloc[i, 1:]
        time = []
        for t in pt_tmp:
            if isinstance(t, str):
                if t is '[]':
                    time.append([0])
                else:
                    t_tmp = t.strip('[]').split(',')
                    print(t_tmp)
                    time.append(list(map(int, t_tmp)))
            else:
                time.append([t])
        processing_time.append(copy.deepcopy(time))
    return job_machine, processing_time, machine_number, operation_number
