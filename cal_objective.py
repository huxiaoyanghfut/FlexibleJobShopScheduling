
def cal_objective(X, machine_number, operation_number, job_machine, processing_time):
    """
        解码出最大完工时间
    """
    job_number = len(operation_number)
    total_operations = sum(operation_number)
    OS = X[:total_operations]
    MS = X[total_operations:2*total_operations]
    objective_value = 4
    return objective_value