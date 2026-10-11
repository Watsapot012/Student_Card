from datetime import datetime

from ..models.student import Student
from ..models.student_card import StudentCard
from .card_validator import CardValidator


class CardService:
    def __init__(self) -> None:
        self._cards: list[StudentCard] = []
        self._validator = CardValidator()

    def create_student(self, **kwargs) -> Student:
        return Student(**kwargs)

    def create_card(
        self,
        student: Student,
        expire_years: int = 4,
        card_type: str = "STUDENT",
        card_number: str = "",
    ) -> StudentCard:
        card = StudentCard(
            student=student,
            expire_years=expire_years,
            card_type=card_type,
            card_number=card_number,
        )
        self._cards.append(card)
        return card

    def get_card_by_student_id(self, student_id: str) -> StudentCard | None:
        return next(
            (card for card in self._cards if card.student.student_id == student_id),
            None,
        )

    def get_all_cards(self) -> list[StudentCard]:
        return list(self._cards)

    def get_active_cards(self) -> list[StudentCard]:
        return [card for card in self._cards if card.is_valid()]

    def validate_card(self, card: StudentCard) -> dict:
        return self._validator.validate_card(card)

    def renew_card(self, card: StudentCard, additional_years: int = 4) -> StudentCard:
        card.issue_date = datetime.now()
        card.expire_years = additional_years
        return card

    def get_statistics(self) -> dict[str, int]:
        total = len(self._cards)
        active = len(self.get_active_cards())
        return {"total_cards": total, "active_cards": active, "expired_cards": total - active}