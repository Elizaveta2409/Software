
data = input().split()
n = int(data[0])
m = int(data[1])
k = int(data[2])
# Читаем исходный массив
a = list(map(int, input().split()))

# Максимальное значение (по условию a_i ≤ 10^5)
MAX_VAL = 100000
freq = [0] * (MAX_VAL + 1)

for num in a:
    freq[num] += 1

for _ in range(m):
    c, x = map(int, input().split())
    freq[x] += c

count = 0
result = 0

for num in range(1, MAX_VAL + 1):
    count += freq[num]
    if count >= k:
        result = num
        break

print(result)