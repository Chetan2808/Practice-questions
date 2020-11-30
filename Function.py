def number_pattern():
    rows = 5
    for i in range(1, rows + 1):
        for b in range(i):
            print(b + 1, end="")
        print()
def odd_even():
    number = int(input())
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")