# ระบบบัตรนักศึกษา

ตัวอย่างโปรเจกต์ Python OOP สำหรับเก็บข้อมูลนักศึกษา ตรวจสอบบัตร และสร้างหน้า HTML สำหรับแสดงหรือพิมพ์บัตร

## เริ่มใช้งาน

```powershell
python -m pip install -r requirements.txt
python main.py
```

เปิดไฟล์ `student_card.html` ที่สร้างขึ้นเพื่อดูบัตร หากต้องการใส่รูป ให้วางรูปไว้ใน `assets/photos/default.jpg` หรือกำหนดตัวแปร `STUDENT_PHOTO_DATA_URI` เป็นค่า data URI ของรูปก่อนรัน

## ทดสอบ

```powershell
python -m pytest tests -v
```

โครงสร้างหลักอยู่ใน `src/models`, `src/services`, `src/views` และ `src/utils`; หน้า HTML อยู่ใน `templates/student_card.html`