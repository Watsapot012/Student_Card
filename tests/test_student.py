from src.models.student import Student


def test_names_and_serialization() -> None:
    student = Student("674259012", "วรรษพจน์", "ศรีพลอยรุ่ง", "Watsapoj", "Sriployrung", "วิศวกรรมซอฟต์แวร์")
    assert student.get_full_name_th() == "วรรษพจน์ ศรีพลอยรุ่ง"
    assert student.get_full_name_en() == "WATSAPOJ SRIPLOYRUNG"
    assert student.to_dict()["student_id"] == "674259012"