# Thai Text Summerization
Use to summerize thai article (prototype)

## Usage
1. ใส่บทความที่ต้องการจะสรุปลงใน input.txt
2. เข้าไปที่ folder ชื่อ thai-sent_tokenize แล้วรันไฟล์ run.py เพื่อทำการตัดประโยค
3. กลับมาที่โฟลเดอร์ thai_text_summerization แล้วทำการรันไฟล์ TextSummerization.py
4. ดูผลลัพธ์ที่ไฟล์ summerize.txt (default สรุป 2 ประโยค สามารถเปลี่ยนจำนวนประโยคได้ที่ param ของ function summarize)

## Requirements
- python 3
- pip
	- tensorflow
	- emoji
	- nltk
	- deepcut

## CR.
- Library ตัดประโยคภาษาไทย (https://github.com/wannaphongcom/thai-sent_tokenize)
- บทความและโค้ดการสรุปบทความ (https://glowingpython.blogspot.com/2014/09/text-summarization-with-nltk.html)
