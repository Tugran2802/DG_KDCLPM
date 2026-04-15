def check_even_odd(n, inputs):
    result = []

    for i in range(n):
        x = inputs[i]

        if x % 2 == 0:
            result.append(f"{x} là số chẵn")
        else:
            result.append(f"{x} là số lẻ")

    return result

if __name__ == "__main__":
    n = int(input("Nhập số lượng số: "))
    inputs = []

    for i in range(n):
        inputs.append(int(input(f"Nhập số thứ {i+1}: ")))

    output = check_even_odd(n, inputs)

    for line in output:
        print(line)