import os
import django

# 1. ตั้งค่าให้ไฟล์นี้เรียกใช้ระบบของ Django ได้
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uncleshop.settings')
django.setup()

from shop.models import Product

# 2. รายการข้อมูลสินค้าทั้งหมด (ใส่กี่ชิ้นก็ได้ในนี้)
sushi_data = [
    {
        "name": "ไดฟุกุสตรอว์เบอร์รี",
        "description": "แป้งโมจินุ่มหนึบ สอดไส้ถั่วแดงหวานละมุนและสตรอว์เบอร์รีสดลูกโตเปรี้ยวอมหวาน",
        "price": 45.00,
        "image": "products/dessert_1.jpg"
    },
    {
        "name": "มิตาราชิดังโงะ",
        "description": "แป้งข้าวจ้าวปั้นย่างเตาถ่าน หอมกลิ่นไหม้อ่อนๆ ราดซอสซีอิ๊วหวานเค็มกลมกล่อม",
        "price": 35.00,
        "image": "products/dessert_2.jpg"
    },
    {
        "name": "โดรายากิ",
        "description": "แพนเค้กเนื้อนุ่มสไตล์ญี่ปุ่น สอดไส้ถั่วแดงกวนบดหยาบ หวานกำลังดี",
        "price": 40.00,
        "image": "products/dessert_3.jpg"
    },
    {
        "name": "ไทยากิไส้คัสตาร์ด",
        "description": "ขนมปังรูปปลาอบร้อน กรอบนอกนุ่มใน สอดไส้ครีมคัสตาร์ดหอมกลิ่นวานิลลา",
        "price": 30.00,
        "image": "products/dessert_4.jpg"
    }
]

# 3. สั่งบันทึกลง Database รวดเดียว
for item in sushi_data:
    Product.objects.update_or_create(
        name=item["name"],
        defaults={
            "description": item["description"],
            "price": item["price"],
            "image": item["image"],
            "is_active": True
        }
    )

print("นำเข้าข้อมูลสินค้าทั้งหมดสำเร็จเรียบร้อย!")