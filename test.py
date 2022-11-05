def primenumbers(n):
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)

def main():
    primenumbers(100)   

if __name__ == "__main__":
    main()