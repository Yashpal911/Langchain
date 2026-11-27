import time

def time_period(func):
    def wrapper(*arg, **kwargs):
        start_time = time.time()
        result = func(*arg, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time
        print("Total time taken to complete: ", round(total_time, 2))
        return result
    return wrapper