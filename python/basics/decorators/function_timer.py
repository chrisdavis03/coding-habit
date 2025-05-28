from time import perf_counter

def time_me(func):
    def wrapper():
        # Start the stopwatch / counter
        start_time = perf_counter()
        func()
        # Stop the stopwatch / counter
        stop_time = perf_counter()
        print (f"elasped time:\t{start_time - stop_time}")
    return wrapper