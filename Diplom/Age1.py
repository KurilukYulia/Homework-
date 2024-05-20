from datetime import datetime


def parse_date(date_str):
    formats = ['%d.%m.%Y', '%d/%m/%Y', '%d %m %Y', '%d-%m-%Y']
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            pass
    raise ValueError(f"Incorrect date format: {date_str}")


def calculate_age(birth_date):
    today = datetime.now()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age
