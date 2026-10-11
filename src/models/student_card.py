from dataclasses import dataclass, field
from datetime import datetime, timedelta
import secrets

from .student import Student


@dataclass
class StudentCard:
    student: Student
    card_number: str = ""
    cvv: str = field(default_factory=lambda: f"{secrets.randbelow(900) + 100}", repr=False)
    issue_date: datetime = field(default_factory=datetime.now)
    expire_years: int = 4
    card_type: str = "STUDENT"

    def __post_init__(self) -> None:
        if not self.card_number:
            self.card_number = self._generate_card_number()

    @staticmethod
    def _generate_card_number() -> str:
        prefix = "6742"
        body = prefix + "".join(str(secrets.randbelow(10)) for _ in range(11))
        for check_digit in range(10):
            candidate = body + str(check_digit)
            if StudentCard._passes_luhn(candidate):
                return " ".join(candidate[index:index + 4] for index in range(0, 16, 4))
        raise RuntimeError("Unable to generate a valid card number")

    @staticmethod
    def _passes_luhn(card_number: str) -> bool:
        digits = [int(digit) for digit in card_number]
        checksum = 0
        for index, digit in enumerate(reversed(digits)):
            if index % 2:
                digit *= 2
                if digit > 9:
                    digit -= 9
            checksum += digit
        return checksum % 10 == 0

    @property
    def expire_date(self) -> datetime:
        return self.issue_date + timedelta(days=self.expire_years * 365)

    @property
    def expire_date_thai(self) -> str:
        thai_year_short = self.expire_date.year + 543 - 2500
        return f"{self.expire_date:%m}/{thai_year_short:02d}"

    @property
    def formatted_card_number(self) -> str:
        digits = "".join(character for character in self.card_number if character.isdigit())
        if len(digits) == 16:
            return " ".join(digits[index:index + 4] for index in range(0, 16, 4))
        return self.card_number

    def is_expired(self) -> bool:
        return datetime.now() > self.expire_date

    def is_valid(self) -> bool:
        return not self.is_expired()

    def get_days_until_expire(self) -> int:
        return max(0, (self.expire_date - datetime.now()).days)

    def to_dict(self) -> dict:
        return {
            "card_number": self.formatted_card_number,
            "issue_date": self.issue_date.isoformat(),
            "expire_date": self.expire_date.isoformat(),
            "expire_date_thai": self.expire_date_thai,
            "card_type": self.card_type,
            "is_valid": self.is_valid(),
            "days_until_expire": self.get_days_until_expire(),
            "student": self.student.to_dict(),
        }

    def __str__(self) -> str:
        return f"StudentCard({self.formatted_card_number} - {self.student.student_id})"