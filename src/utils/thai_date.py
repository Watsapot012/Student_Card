from datetime import datetime


class ThaiDate:
    THAI_MONTHS = [
        "มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน",
        "พฤษภาคม", "มิถุนายน", "กรกฎาคม", "สิงหาคม",
        "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม",
    ]

    @staticmethod
    def to_thai_year(year: int) -> int:
        return year + 543

    @staticmethod
    def to_buddhist_year(year: int) -> int:
        return year + 543 - 2500

    @staticmethod
    def format_thai_date(date: datetime, format_type: str = "full") -> str:
        thai_year = ThaiDate.to_thai_year(date.year)
        month_name = ThaiDate.THAI_MONTHS[date.month - 1]
        if format_type == "full":
            return f"{date.day} {month_name} {thai_year}"
        if format_type == "short":
            return f"{date.day}/{date.month}/{thai_year}"
        if format_type == "card":
            return f"{date:%m}/{ThaiDate.to_buddhist_year(date.year):02d}"
        return str(date)