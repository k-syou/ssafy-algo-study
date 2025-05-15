N = int(input())
arr = [*map(int, input().split())]

positive = [0] * (N + 1)
negative = [0] * (N + 1)

for num in arr:
    if num > 0:
        positive[num] += 1
    else:
        negative[abs(num)] += 1

# negative.reverse()
for i in range(1, N + 1):
    positive[i] += positive[i - 1]
    negative[-i - 1] += negative[-i]
# negative.reverse()

result = []
for i in range(N + 1):
    liar_count = N - positive[i] - negative[i]
    if liar_count == i:
        result.append(i)

print(len(result))
print(*result)
