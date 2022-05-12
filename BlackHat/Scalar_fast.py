def bits(n):
    """
    Генерирует двоичные разряды n, начиная
    с наименее значимого бита.

    bits(151) -> 1, 1, 1, 0, 1, 0, 0, 1
    """
    while n:
        yield n & 1
        n >>= 1

def double_and_add(n, x):
    """
    Возвращает результат n * x, вычисленный
    алгоритмом удвоения-сложения.
    """
    result = 0
    addend = x

    for bit in bits(n):
        if bit == 1:
            result += addend
        addend *= 2
    return result

def main():
    import time
    tic = time.perf_counter_ns()
    print(double_and_add(127, 127.127))
    toc = time.process_time_ns()
    print(toc - tic)
    tic = 0
    toc = 0
    tic = time.perf_counter_ns()
    print(127 * 127.127)
    toc = time.process_time_ns()
    print(toc - tic)

if __name__ == '__main__':
    main()
