import sys

from stats import average_by_city, read_valid, warmest_city


def main() -> None:
    lines = sys.stdin.read().splitlines()

    records = read_valid(lines)

    non_empty = [ln for ln in lines if ln.strip()]

    skipped = len(non_empty) - len(records)

    averages = average_by_city(records)
    best = warmest_city(records)

    print(len(records))
    print(skipped)
    if best:
        print(f"{averages[best]:.1f}")
    else:
        print("0.0")


if __name__ == "__main__":
    main()