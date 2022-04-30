import math

def main():
    try:
        x = int(input()) #conflict for testing
        print(math.factorial(x))
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
