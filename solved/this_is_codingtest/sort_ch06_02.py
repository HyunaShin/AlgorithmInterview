n = int(input())
numbers = [ int(input()) for _ in range(n)]
pivot_idx = 0

def quick_sort(numbers):
    if len(numbers) <=1:
        return numbers
    left = list(filter(lambda x : x > numbers[pivot_idx], numbers[pivot_idx:]))
    right = list(filter(lambda x: x < numbers[pivot_idx], numbers[pivot_idx:]))
    return quick_sort(left) + [numbers[pivot_idx]] + quick_sort(right)

ans = quick_sort(numbers)
print(ans)
