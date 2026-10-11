from html import escape
from pathlib import Path
from string import Template

from ..models.student_card import StudentCard


class CardRenderer:
    def __init__(self, card: StudentCard, template_path: Path | None = None) -> None:
        self.card = card
        self.student = card.student
        self.template_path = template_path or Path(__file__).resolve().parents[2] / "templates" / "student_card.html"

    def render_html(self) -> str:
        template = Template(self.template_path.read_text(encoding="utf-8"))
        student = self.student
        if student.photo_path.startswith("data:image/"):
            photo_src = student.photo_path
        else:
            photo_path = Path(student.photo_path)
            if not photo_path.is_absolute():
                photo_path = Path(__file__).resolve().parents[2] / photo_path
            photo_src = photo_path.resolve().as_uri() if photo_path.is_file() else ""
        logo_path = Path(__file__).resolve().parents[2] / "assets" / "photos" / "Npru-logo.png"
        logo_src = logo_path.resolve().as_uri() if logo_path.is_file() else ""

        return template.safe_substitute(
            title=escape(student.get_full_name_th()),
            logo_src=escape(logo_src, quote=True),
            university_th=escape(student.university_th),
            university_en=escape(student.university_en),
            photo_src=escape(photo_src, quote=True),
            photo_display="block" if photo_src else "none",
            photo_empty_display="none" if photo_src else "block",
            name_th=escape(f"{student.get_prefix_th()} {student.get_full_name_th()}"),
            name_en=escape(f"{student.get_prefix_en()} {student.get_full_name_en()}"),
            student_id=escape(student.student_id),
            faculty=escape(student.faculty),
            card_number=escape(self.card.formatted_card_number),
            expire_date=escape(self.card.expire_date_thai),
        )

    def render_text(self) -> str:
        return "\n".join(
            (
                self.student.university_th,
                f"ชื่อ-สกุล: {self.student.get_prefix_th()} {self.student.get_full_name_th()}",
                f"Name: {self.student.get_prefix_en()} {self.student.get_full_name_en()}",
                f"รหัสนักศึกษา: {self.student.student_id}",
                f"สาขาวิชา: {self.student.faculty}",
                f"Card Number: {self.card.formatted_card_number}",
                f"Valid Thru: {self.card.expire_date_thai}",
                f"Status: {'VALID' if self.card.is_valid() else 'EXPIRED'}",
            )
        )