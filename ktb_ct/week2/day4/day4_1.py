n = int(input())

for _ in range(n):
    numbers = list(map(int, input().split()))
    numbers.sort(reverse=True)
    print(numbers[2])