def generate_binary_strings(n, results=''):
    if len(results) == n:
        print(results)
        return
    generate_binary_strings(n, results + '0')
    generate_binary_strings(n, results + '1')

if __name__ == "__main__":
    n = 8
    generate_binary_strings(n)
