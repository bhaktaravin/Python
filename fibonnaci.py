def main():
    n = int(input("Enter a number: "))
    run(n)

def run(n):
    if n == 1 or n == 0:
        a = 1
        return a
    else:
        a = 1
        b = 0
        for c in range(0, n):
            tmp = a 
            a = b
            b = tmp + b
            print(a)

if __name__ == "__main__":
    main()

