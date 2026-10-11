from src.models.student import Student
from src.services.card_service import CardService
from src.services.card_validator import CardValidator


def test_service_lifecycle_and_statistics() -> None:
    service = CardService()
    student = Student("674259012", "วรรษพจน์", "ศรีพลอยรุ่ง", "Watsapoj", "Sriployrung", "วิศวกรรมซอฟต์แวร์")
    card = service.create_card(student, card_number="4732 5285 1820 5940")
    assert service.get_card_by_student_id(student.student_id) is card
    assert service.validate_card(card)["is_valid"]
    assert service.get_statistics() == {"total_cards": 1, "active_cards": 1, "expired_cards": 0}
    service.renew_card(card, additional_years=5)
    assert card.expire_years == 5


def test_luhn_validation_is_separate_from_card_record_validation() -> None:
    assert CardValidator.validate_card_number("4111 1111 1111 1111")
    assert not CardValidator.validate_card_number("1234 5678 9012 3456")
    assert not CardValidator.validate_card_number("4111-x111-1111-1111")