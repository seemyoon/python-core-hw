# Example. Work in parallel, but in what order is unpredictable.
import threading  # for work with threads

print(threading.current_thread())  # show current thread


def for_thread(a, b):
    for i in range(100):
        print('values:', a, b)


thread = threading.Thread(target=for_thread, args=(5, 6), name='for_thread')
# creates a new thread, where:

# target=for_thread — the function that will be executed in this thread,
# args=(5, 6) — arguments that are passed to the for_thread function,
# name='for_thread' — the name of the thread (optional, but useful for debugging).

thread.start()

for i in range(100):
    print('hello')
