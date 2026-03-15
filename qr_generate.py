import qrcode
import pandas as pd
import os

# Read students from CSV
students = pd.read_csv("students.csv")

# Create folder for QR codes
if not os.path.exists("qr_codes"):
    os.makedirs("qr_codes")

# Generate QR codes for all students
for index, row in students.iterrows():

    student_id = row["student_id"]
    name = row["name"]

    data = f"{student_id},{name}"

    img = qrcode.make(data)

    file_path = f"qr_codes/{student_id}.png"
    img.save(file_path)

    print(f"QR generated for {name}")

print("All QR codes generated successfully!")