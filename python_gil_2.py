import threading
import timeit

class WorkerClass:
    def __init__(self):
        self.counter = 0

    def work(self):
        for _ in range(10000000):
            self.counter += 1

def run_threads(num_workers):
    workers = [WorkerClass() for _ in range(num_workers)]
    threads = []

    for worker in workers:
        thread = threading.Thread(target=worker.work)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def run_sequential(num_workers):
    workers = [WorkerClass() for _ in range(num_workers)]

    for worker in workers:
        worker.work()

def benchmark_threads():
    run_threads(5)

def benchmark_sequential():
    run_sequential(5)

if __name__ == "__main__":
    threads_time = timeit.timeit(benchmark_threads, number=5)
    sequential_time = timeit.timeit(benchmark_sequential, number=5)
    
    print(f"Time taken with threads: {threads_time}s")
    print(f"Time taken sequentially: {sequential_time}s")

