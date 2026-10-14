levels = {"DEBUG", "INFO", "WARNING", "ERROR"}


def parse_event(line: str) -> dict:
    parts = line.strip().split(maxsplit=2)
    if len(parts) != 3:
        raise ValueError(f"не удалось разобрать строку: {line!r}")

    time, level, message = parts
    if level not in levels:
        raise ValueError(f"неизвестный уровень: {level!r}")

    return {"time": time, "level": level, "message": message}


def count_levels(lines) -> dict:
    """Посчитать строки каждого уровня. Испорченные — под ключом BROKEN."""
    counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            key = "BROKEN"
        else:
            key = event["level"]
        counts[key] = counts.get(key, 0) + 1
    return counts


def top_errors(lines, n: int) -> list[list]:
    frequencies = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            continue
        if event["level"] != "ERROR":
            continue
        message = event["message"]
        frequencies[message] = frequencies.get(message, 0) + 1

    ordered = sorted(frequencies.items(), key=lambda pair: (-pair[1], pair[0]))
    return [[message, count] for message, count in ordered[:n]]


def format_report(counts: dict, errors: list[list]) -> str:
    lines = ["Отчёт по журналу", ""]

    for level in sorted(counts):
        lines.append(f"{level}: {counts[level]}")

    lines.append("")
    lines.append("Частые ошибки:")
    for message, count in errors:
        lines.append(f"- {message} — {count}")

    return "\n".join(lines) + "\n"