import os
from pathlib import Path

from src.models.student import Student
from src.services.card_service import CardService
from src.views.card_renderer import CardRenderer


def main() -> None:
    service = CardService()
    student = Student(
        student_id="674259012",
        first_name_th="วรรษพจน์",
        last_name_th="ศรีพลอยรุ่ง",
        first_name_en="Watsapoj",
        last_name_en="Sriployrung",
        faculty="วิศวกรรมซอฟต์แวร์",
        photo_path=os.environ.get("STUDENT_PHOTO_DATA_URI", "assets/photos/รูปนักศึกษา.jpg"),
    )
    card = service.create_card(
        student,
        card_number="4732 5285 1820 5940",
        card_type="STUDENT",
    )
    result = service.validate_card(card)
    output = Path(__file__).resolve().parent / "student_card.html"
    output.write_text(CardRenderer(card).render_html(), encoding="utf-8")
    print(f"สร้างบัตรแล้ว: {output}")
    print(f"ตรวจสอบข้อมูล: {'ผ่าน' if result['is_valid'] else 'ไม่ผ่าน'}")
    for warning in result["warnings"]:
        print(f"คำเตือน: {warning}")
    for error in result["errors"]:
        print(f"ข้อผิดพลาด: {error}")


if __name__ == "__main__":
    main()