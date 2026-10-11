from datetime import datetime, timedelta

from src.models.student import Student
from src.models.student_card import StudentCard


def make_student() -> Student:
    return Student("674259012", "วรรษพจน์", "ศรีพลอยรุ่ง", "Watsapoj", "Sriployrung", "วิศวกรรมซอฟต์แวร์")


def test_card_number_format_and_expiry() -> None:
    card = StudentCard(make_student(), card_number="4732528518205940")
    assert card.formatted_card_number == "4732 5285 1820 5940"
    assert card.is_valid()
    assert len(card.cvv) == 3


def test_expired_card() -> None:
    card = StudentCard(make_student(), issue_date=datetime.now() - timedelta(days=5 * 365))
    assert card.is_expired()
    assert card.get_days_until_expire() == 0