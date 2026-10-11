from datetime import datetime

from src.utils.thai_date import ThaiDate


def test_thai_date_formats() -> None:
    date = datetime(2026, 10, 5)
    assert ThaiDate.to_thai_year(2026) == 2569
    assert ThaiDate.format_thai_date(date, "full") == "5 ตุลาคม 2569"
    assert ThaiDate.format_thai_date(date, "short") == "5/10/2569"
    assert ThaiDate.format_thai_date(date, "card") == "10/69"