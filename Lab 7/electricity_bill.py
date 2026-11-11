RATES = {"DOM": 3, "COM": 6}
SLAB = {"A": 1, "B": 2}

def units_consumed(reading):
    if not isinstance(reading, str):
        return None
    parts = reading.strip().split(':')
    if len(parts) != 2:
        return None
    try:
        previous = int(parts[0].strip())
        current = int(parts[1].strip())
        if previous < 0 or current < 0 or current < previous:
            return None
        return current - previous
    except (ValueError, TypeError):
        return None

def daily_average(units_csv):
    if not isinstance(units_csv, str):
        return None
    parts = [u.strip() for u in units_csv.split(',') if u.strip()]
    if not parts:
        return None
    try:
        units = [int(u) for u in parts]
        if any(u < 0 for u in units):
            return None
        return round(sum(units) / len(units), 2)
    except (ValueError, TypeError):
        return None

def tariff_rate(code):
    if not isinstance(code, str):
        return None
    parts = code.strip().split('-')
    if len(parts) != 2:
        return None
    category = parts[0].strip().upper()
    slab = parts[1].strip().upper()
    if category not in RATES or slab not in SLAB:
        return None
    return RATES[category] * SLAB[slab]

def main():
    print("==== Running units_consumed ====")
    user_input = input("Enter meter readings as previous:current (e.g. 1200:1350): ")
    result = units_consumed(user_input)
    print("Units Consumed:", result)

    print("\n==== Running daily_average ====")
    user_input = input("Enter daily units as CSV (e.g. 5,7,6): ")
    result = daily_average(user_input)
    print("Daily Average:", result)

    print("\n==== Running tariff_rate ====")
    user_input = input("Enter a tariff code (e.g. DOM-A): ")
    result = tariff_rate(user_input)
    print("Rate per Unit:", result)

if __name__ == "__main__":
    main()
