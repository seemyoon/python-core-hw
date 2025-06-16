# Example.
# If we want threads work in parallel and when multiple threads modify the same variable (for example, count += 1), a race condition occurs.
import threading
import time

start = time.time()
count = 0

lock = threading.Lock()


# Lock prevents threads from changing variables at the same time, making the critical section thread-safe.

def inc():
    with lock:
        # When threads enter with lock: - there is no longer parallelism inside this block,
        # because only one thread can be inside with lock: at any given time.
        global count
        count += 1
        print(count)


threads = []

for _ in range(1000):
    #     inc()
    thread = threading.Thread(target=inc)
    threads.append(
        thread)  # Why add threads to the threads = [] list? So that you can then iterate over them and call .join() on each one.
    thread.start()

for thread in threads:
    thread.join()

end = time.time()

print(f"Execution time: {end - start:.4f} seconds")
