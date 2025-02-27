def count_favourite_singers(n, singers):
    singer_counts = {}
    for singer in singers:
        if singer in singer_counts:
            singer_counts[singer] += 1
        else:
            singer_counts[singer] = 1

    max_count = max(singer_counts.values())
    favourite_singers = sum(1 for count in singer_counts.values() if count == max_count)

    return favourite_singers

n = int(input())
singers = list(map(int, input().split()))

favourite_singers = count_favourite_singers(n, singers)

print(favourite_singers)