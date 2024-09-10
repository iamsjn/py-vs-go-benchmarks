package main

import (
	"fmt"
	"sync"
	"time"
)

type Worker struct {
	counter int
}

func (w *Worker) work() {
	for i := 0; i < 10000000; i++ {
		w.counter++
	}
}

func runGoroutines(numWorkers int) {
	var wg sync.WaitGroup
	wg.Add(numWorkers)

	for i := 0; i < numWorkers; i++ {
		worker := Worker{}
		go func() {
			defer wg.Done()
			worker.work()
		}()
	}

	wg.Wait() 
}

func runSequential(numWorkers int) {
	for i := 0; i < numWorkers; i++ {
		worker := Worker{}
		worker.work()
	}
}

func main() {
	start := time.Now()
	runGoroutines(5)
	goroutinesDuration := time.Since(start)
	fmt.Printf("Time taken with goroutines: %v\n", goroutinesDuration)

	start = time.Now()
	runSequential(5)
	sequentialDuration := time.Since(start)
	fmt.Printf("Time taken sequentially: %v\n", sequentialDuration)
}

