import random
from concurrent.futures import ProcessPoolExecutor

def _count_inside(d, R, n_samples):
    """Hjälpfunktion som körs i varje subprocess."""
    count = 0
    for _ in range(n_samples):
        # slumpa en punkt i d dimensioner
        point = [random.uniform(-R, R) for _ in range(d)]
        # kolla om punkten ligger inom enhetssfären
        if sum(x*x for x in point) < R*R:
            count += 1
    return count

def sphere_volume_parallel(n, d, R=1, n_workers=4):
    # dela upp n på n_workers-delar (viss rest hanteras i sista chunk)
    base, rest = divmod(n, n_workers)
    chunks = [base + (1 if i < rest else 0) for i in range(n_workers)]
    print(chunks)
    # Kör parallellt
    with ProcessPoolExecutor(max_workers=n_workers) as exec:
        # varje future räknar sin delmängd
        futures = [
            exec.submit(_count_inside, d, R, chunk)
            for chunk in chunks
        ]
        # samla ihop resultaten
        total_inside = sum(f.result() for f in futures)

    # Monte Carlo‐estimat
    return (2*R)**d * (total_inside / n)
