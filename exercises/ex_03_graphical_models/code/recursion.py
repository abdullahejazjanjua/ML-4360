def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fib(n-1) + fib(n-2) 

print(f"Fib of 3: {fib(3)}")

# fib(4):
# fib(3) + fib(2)
# fib(3):
# fib(2) + fib(1) -> 1 + 1 = 2
# fib(2):
# fib(1) + fib(0) -> 1 + 0 = 1

def dec_to_bin(num: int, ans: str = "") -> str:
    if num == 0:
        return ans
    ans += str(num % 2)
    return dec_to_bin(num // 2, ans)

print(f"Binary of 2: {dec_to_bin(2)[::-1]}")

# dec_to_bin(2)
# print(2%2) -> 0
# dec_to_bin(2//2):
# print(1%2) -> 1
# dec_to_bin(1 // 2) -> 0 = 0
# num == 0: return = 0