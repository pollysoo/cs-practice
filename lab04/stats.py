def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError(f"Ожидалось 3 поля, получено {len(parts)}: {line!r}")

    city, temp_str, date = parts
    city = city.strip()
    temp_str = temp_str.strip()
    date = date.strip()

    if not city or not date:
        raise ValueError(f"Пустой город или дата: {line!r}")

    temp_str = temp_str.replace(",", ".")

    try:
        temp = float(temp_str)
    except ValueError as exc:
        raise ValueError(
            f"Температура не является числом: {temp_str!r}"
        ) from exc

    return {"city": city, "temperature": temp, "date": date}


def read_valid(lines: list[str]) -> list[dict]:
    records: list[dict] = []
    for line in lines:
        if not line.strip():
            continue
        try:
            records.append(parse_record(line))
        except ValueError:
            pass
    return records


def average_by_city(records: list[dict]) -> dict:
    total: dict[str, float] = {}
    count: dict[str, int] = {}
    for rec in records:
        city = rec["city"]
        total[city] = total.get(city, 0.0) + rec["temperature"]
        count[city] = count.get(city, 0) + 1
    return {city: round(total[city] / count[city], 1) for city in total}


def warmest_city(records: list[dict]) -> str:
   
    averages = average_by_city(records)
    if not averages:
        return ""
    best = ""
    for city in sorted(averages):
        if best == "" or averages[city] > averages[best]:
            best = city
    return best