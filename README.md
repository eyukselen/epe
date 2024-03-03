# eprofiler

Execution profiler

a simple tool to monitor execution times of functions.

import `timeit` function and use as a decorator for the function you want to monitor
if you pass an empty dict to it as below, you can get the results and use it in code.
otherwise it will print duration.


## usage:
```
from eprofiler import timeit

print("without stats dict provided")


@timeit()
def my_func_to_test():
    for x in range(100000):
        y = x ^ 2


my_func_to_test()
stats = {}

print("without stats dict provided")


@timeit(stats)
def my_func_to_test_with_stats():
    for x in range(100000):
        y = x ^ 2


my_func_to_test_with_stats()
print(stats)
```

