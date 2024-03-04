Usage of eprofiler
================================

To use eprofiler, import `timeit` function and use it as a decorator for the function you want to monitor. If you pass an empty dictionary to it as below, you can get the results and use it in code; otherwise, it will print duration.

.. code-block:: python

    from eprofiler import timeit

    print("Without stats dict provided")

    @timeit()
    def my_func_to_test():
        for x in range(100000):
            y = x ^ 2

    my_func_to_test()
    stats = {}

    print("With stats dict provided")

    @timeit(stats)
    def my_func_to_test_with_stats():
        for x in range(100000):
            y = x ^ 2

    my_func_to_test_with_stats()
    print(stats)