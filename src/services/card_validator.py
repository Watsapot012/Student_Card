from typing import Any

from ..models.student_card import StudentCard


class CardValidator:
    @staticmethod
    def validate_card(card: StudentCard) -> dict[str, Any]:
        errors: list[str] = []
        warnings: list[str] = []
        student = card.student

        if not student.student_id:
            errors.append("รหัสนักศึกษาว่างเปล่า")
        elif len(student.student_id) < 8:
            errors.append("รหัสนักศึกษาต้องมีความยาวอย่างน้อย 8 หลัก")
        if not student.first_name_th or not student.last_name_th:
            errors.append("ชื่อ-สกุลภาษาไทยไม่ครบถ้วน")
        if not student.first_name_en or not student.last_name_en:
            errors.append("ชื่อ-สกุลภาษาอังกฤษไม่ครบถ้วน")

        digits = "".join(character for character in card.card_number if character.isdigit())
        if len(digits) != 16:
            errors.append("หมายเลขบัตรต้องมีความยาว 16 หลัก")
        if card.is_expired():
            errors.append("บัตรหมดอายุแล้ว")
        elif card.get_days_until_expire() < 30:
            warnings.append("บัตรจะหมดอายุภายใน 30 วัน")

        return {"is_valid": not errors, "errors": errors, "warnings": warnings}

    @staticmethod
    def validate_card_number(card_number: str) -> bool:
        digits = card_number.replace(" ", "")
        if not digits.isdigit() or len(digits) != 16:
            return False
        total = 0
        for index, character in enumerate(reversed(digits)):
            digit = int(character)
            if index % 2:
                digit *= 2
                if digit > 9:
                    digit -= 9
            total += digit
        return total % 10 == 0