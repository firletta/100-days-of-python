import time


def speed_calc_decorator(function):
    def wrapper():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"Function '{function.__name__}' executed in: {end_time - start_time:.4f} seconds")

    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(10_000_000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10_000_000):
        i * i


if __name__ == "__main__":
    current_time = time.time()
    print(f"Current timestamp: {current_time}")

    fast_function()
    slow_function()
