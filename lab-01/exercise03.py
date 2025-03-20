import functions as f
# 3. If-then-else statements - O(n)
def if_then_else(n):
    """Algorithm with conditional O(n) complexity"""
    if n % 2 == 0:
        for _ in range(n):
            pass
    else:
        for _ in range(n):
            pass

log_condt= [1,10,100,1000,10000,100000]

f.run_algorithm(if_then_else,log_condt,'Linear Complexity')



