def fibonacci(max: int):        # генератор последовательности
    a, b = 0, 1
    while a < max:
        yield a                 # возвращаем a, + запоминаем место для следующего вызова
        a, b = b, a + b         # параллельное присваивание


def output_even_numbers(k: int, result=[]):
    max = k
    while len(result) < k:
        max = max + 1
        for n in fibonacci(max):              # используем генератор fibonacci() как итератор
            if n%2 == 0 and n not in result: result.append(n)
            else: continue
    return result


if __name__=='__main__':
    k = input('Введите количество четных элементов необходимых для вывода: ')
    [print(n, end='') if n == output_even_numbers(int(k))[-1] else print(n, end=',') for n in output_even_numbers(int(k))]
