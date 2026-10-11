import sys
from stats import average_by_city, read_valid, warmest_city

lines = sys.stdin.read().splitlines()
records = read_valid(lines)
bad = 0

for line in lines:
    if line.strip() == "":
        continue

    try:
        from stats import parse_record
        parse_record(line)
    except ValueError:
        bad += 1

averages = average_by_city(records)
city = warmest_city(records)

print(len(records))
print(bad)

if city == "":
    print("0.0")
else:
    print(f"{averages[city]:.1f}")