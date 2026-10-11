def parse_record(line: str) -> dict:
    parts = line.split(";")

    if len(parts) != 3:
        raise ValueError("Должно быть три поля")

    city = parts[0].strip()
    temp = parts[1].strip()
    date = parts[2].strip()

    if city == "" or date == "":
        raise ValueError("Пустой город или дата")

    try:
        temp = float(temp)
    except ValueError:
        raise ValueError("Температура должна быть числом")

    return {"city": city, "temp": temp, "date": date}

def read_valid(lines: list[str]) -> list[dict]:
    records = []

    for line in lines:
        if line.strip() == "":
            continue

        try:
            record = parse_record(line)
            records.append(record)
        except ValueError:
            continue

    return records

def average_by_city(records: list[dict]) -> dict:
    total = {}
    count = {}

    for record in records:
        city = record["city"]
        temp = record["temp"]

        total[city] = total.get(city, 0) + temp
        count[city] = count.get(city, 0) + 1

    averages = {}

    for city in total:
        averages[city] = round(total[city] / count[city], 1)

    return averages

def warmest_city(records: list[dict]) -> str:
    averages = average_by_city(records)

    if not averages:
        return ""

    best = sorted(averages)[0]

    for city in averages:
        if averages[city] > averages[best]:
            best = city

    return best

