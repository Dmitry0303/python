for i in range(32, 128):
    print(f"{i:3}: {chr(i):3}  ", end='')
    if (i - 1) % 10 == 0:
        print()
