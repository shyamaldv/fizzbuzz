def main():
    user_input = int(input("Number to count to: "))
    fizzbuzz(user_input)

def fizzbuzz(n):
    for i in range(n + 1):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 5 == 0 and i % 3 == 0:
            print("Fizzbuzz")
        else:
            print(i) 


if __name__ == '__main__':
    main()
