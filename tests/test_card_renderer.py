from src.models.student import Student
from src.models.student_card import StudentCard
from src.views.card_renderer import CardRenderer


def test_render_html_contains_student_fields() -> None:
    student = Student("674259012", "วรรษพจน์", "ศรีพลอยรุ่ง", "Watsapoj", "Sriployrung", "วิศวกรรมซอฟต์แวร์")
    card = StudentCard(student, card_number="4732 5285 1820 5940")
    html = CardRenderer(card).render_html()
    assert "วรรษพจน์ ศรีพลอยรุ่ง" in html
    assert "674259012" in html
    assert "4732 5285 1820 5940" in html
    assert "CVV" not in html