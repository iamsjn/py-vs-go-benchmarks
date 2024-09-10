import threading
import timeit

class CommonClass:
    def __init__(self):
        self.counter = 0

    def increment(self):
        for _ in range(1000000):
            self.counter += 1

class ClassOne:
    def __init__(self, common_instance):
        self.common_instance = common_instance

    def run(self):
        self.common_instance.increment()

class ClassTwo:
    def __init__(self, common_instance):
        self.common_instance = common_instance

    def run(self):
        self.common_instance.increment()

def run_threads_separately(common_instance):
    class_one = ClassOne(common_instance)
    class_two = ClassTwo(common_instance)
    
    thread1 = threading.Thread(target=class_one.run)
    thread2 = threading.Thread(target=class_two.run)
    
    thread1.start()
    thread1.join()
    
    thread2.start()
    thread2.join()

def run_threads_simultaneously(common_instance):
    class_one = ClassOne(common_instance)
    class_two = ClassTwo(common_instance)
    
    thread1 = threading.Thread(target=class_one.run)
    thread2 = threading.Thread(target=class_two.run)
    
    thread1.start()
    thread2.start()
    
    thread1.join()  
    thread2.join()

def benchmark_separate():
    common_instance = CommonClass()
    run_threads_separately(common_instance)

def benchmark_simultaneous():
    common_instance = CommonClass()
    run_threads_simultaneously(common_instance)

if __name__ == "__main__":
    separate_time = timeit.timeit(benchmark_separate, number=5)
    simultaneous_time = timeit.timeit(benchmark_simultaneous, number=5)
    
    print(f"Time taken with separate access: {separate_time}")
    print(f"Time taken with simultaneous access: {simultaneous_time}")

