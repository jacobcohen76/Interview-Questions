import memory_profiler
import time

from typing import Any, Callable, Dict, Tuple, Type

class Profiler:
    ReturnType = Type['ReturnType']

    def __init__(self,
            interval: float = 0.01,
            timeout: float = None,
            max_iterations: int = None,
            include_children: bool = False,
            multiprocess: bool = False,
        ):
        self.interval = interval
        self.timeout = timeout
        self.max_iterations = max_iterations
        self.include_children = include_children
        self.multiprocess = multiprocess
    
    def profile(self,
            function: Callable[..., ReturnType], *args, **kwargs,
        ) -> Tuple[ReturnType, float, float]:
        perf_start = time.perf_counter()
        mem_usage, ret_val = memory_profiler.memory_usage(
            proc=(function, args, kwargs),
            retval=True,
            max_usage=True,
            interval=self.interval,
            timeout=self.timeout,
            max_iterations=self.max_iterations,
            include_children=self.include_children,
            multiprocess=self.multiprocess,
        )
        perf_time = time.perf_counter() - perf_start
        return ret_val, perf_time, mem_usage