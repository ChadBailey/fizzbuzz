def fizzbuzz(number, end):
    assert type(number) == int, f"Expected an integer, got {type(number)}"
    assert type(end) == int, f"Expected an integer, got {type(number)}"
    fizz = True if (number % 3) == 0 else False
    buzz = True if (number % 5) == 0 else False
    if fizz and buzz:
        print('FizzBuzz!')
    elif fizz:
        print('Fizz')
    elif buzz:
        print('Buzz')
    else:
        print(number)

    if number == end:
        return
    else:
        fizzbuzz(number+1, end)


if __name__ == '__main__':
    fizzbuzz(1, 100)
