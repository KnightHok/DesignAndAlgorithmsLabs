def max_segments_coverage(segments):
    endpoints = []
    for segment in segments:
        endpoints.append(segment[0])
        endpoints.append(segment[1])

    endpoints.sort()

    current_coverage = 0
    max_coverage = 0

    for endpoint in endpoints:
        if endpoint in [segment[0] for segment in segments]:
            current_coverage += 1
        if endpoint in [segment[1] for segment in segments]:
            current_coverage -= 1

        max_coverage = max(max_coverage, current_coverage)

    return max_coverage


segments = [(-0.3, 2.7), (-1, 0.5), (2.5, 3.3), (-0.7, 2.3), (0.5, 1.7)]
max_coverage = max_segments_coverage(segments)
print(max_coverage)