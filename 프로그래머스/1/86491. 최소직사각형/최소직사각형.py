def solution(sizes):
    for size in sizes:
        size.sort()

    max_width = max(size[0] for size in sizes)
    max_height = max(size[1] for size in sizes)

    return max_width * max_height
