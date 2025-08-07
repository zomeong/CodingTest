def main():

    n = int(input())
    answer = 0

    while True:
        if n % 5 == 0:
            answer += n // 5
            print(answer)
            break

        n -= 3
        answer += 1

        if n == 0:
            print(answer)
            break
        elif n < 0:
            print(-1)
            break

    return

if __name__ == "__main__":
    main()