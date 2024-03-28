def fun(y):
    print(f"y={y}")
    x = 1
    print(f"x inside fun={x}")

if __name__ == "__main__":
    x = 5
    print(f"initial x outside fun={x}")
    fun(x)
    print(f"x outside fun={x}")
