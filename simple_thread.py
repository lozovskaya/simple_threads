import threading, logging

cv = threading.Condition()
current_number = 1


def thread_function(name, n):
    global cv, current_number

    for i in range(n):
        with cv:
            cv.wait_for(lambda: name == current_number)
            print(name, end="")
            current_number = current_number % 3 + 1
            cv.notify_all()


if __name__ == "__main__":
    # logging.getLogger().setLevel(logging.INFO)
    n = int(input())

    threads = list()
    for index in range(3):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index + 1, n))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)
