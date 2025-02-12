import sys
from collections import Counter


def process_queries(N, K, Q, A, queries):
    diff = [0] * (N + 1)

    results = []

    for query in queries:
        qtype, L, R = map(int, query[:3])
        L -= 1
        R -= 1

        if qtype == 1:
            # 1 L R X -> Range Update
            X = int(query[3])
            diff[L] += X
            if R + 1 < N:
                diff[R + 1] -= X

        elif qtype == 2:

            current_arr = A[:]

            update_value = 0
            for i in range(N):
                update_value += diff[i]
                current_arr[i] += update_value

            subarray = current_arr[L:R + 1]

            remainder_count = Counter(x % K for x in subarray)

            max_freq = max(remainder_count.values())

            results.append(len(subarray) - max_freq)

    sys.stdout.write("\n".join(map(str, results)) + "\n")


def main():
    N, K, Q = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))

    queries = [sys.stdin.readline().split() for _ in range(Q)]

    process_queries(N, K, Q, A, queries)


if __name__ == "__main__":
    main()
