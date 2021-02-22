import numpy as np

nr_of_samples = 10_000


def estimate_pi(accuracy):
    total = accuracy
    points_inside = 0
    all_x = np.random.uniform(0, 1, total)
    all_y = np.random.uniform(0, 1, total)
    for x, y in zip(all_x, all_y):
        distance = x ** 2 + y ** 2
        if distance < 1:
            points_inside += 1
    return 4 * (points_inside / total)


print(estimate_pi(nr_of_samples))
