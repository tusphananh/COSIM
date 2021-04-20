import basic

if __name__ == '__main__':
    while True:
        str = input("Code :")
        tokens, errors = basic.run("hello",str)
        print(errors.toString() if errors else tokens)
