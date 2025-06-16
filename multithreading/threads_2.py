# Example. If we want threads work in parallel and in order.
import threading
import time


def show(n, t):
    for i in range(n):
        print(i, threading.current_thread().name)
        time.sleep(t)


thread_1 = threading.Thread(target=show, args=(4, 0.5), name='thread_1')
thread_2 = threading.Thread(target=show, args=(10, 0.5), name='thread_2')

thread_1.start()
thread_2.start()

# without .join() - threads will be in disorder.
# with .join() - thread_1 => thread_2 => print('hello')

thread_1.join()
thread_2.join()

print('hello')

# we start both threads at the same time, but then wait for each of them to finish, in this order:

# thread_1.join() — the main thread waits for thread_1 to finish.
# thread_2.join() — then waits for thread_2.

# BUT! The threads still work in parallel!
# That is: thread_2 does not wait for thread_1 to finish — it is already running.