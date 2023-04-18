import time

is_terminated = False

targets = [

]


def termination_handler():
    global is_terminated

    # TODO handle termination signal


def main():
    while not is_terminated:
        # TODO collect availability statuses from all targets
        # TODO write results to db

        time.sleep(30)


if __name__ == '__main__':
    main()
