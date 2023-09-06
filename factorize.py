from multiprocessing import Process


def factorize(*number):
    result = []
    for item in number:
        inner_arr = []
        for i in range(1,item +1):
            if item % i == 0:
                inner_arr.append(i)
        result.append(inner_arr)
    return result


if __name__ == '__main__':
    test = (128, 255, 99999, 10651060)
    processes = []
    for i in test:
        pr = Process(target=factorize, args=(test))
        pr.start()
        processes.append(pr)
# 0.484375