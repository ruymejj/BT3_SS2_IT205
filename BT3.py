print("Phòng khám đa khoa Sức Khỏe Vàng")

name_patient = input("Nhập tên của bệnh nhân: ")
age_patient = int(input("Nhập tuổi của bệnh nhân: "))

if age_patient < 6:
    result = "PRIORITY: Pediatric patients - Direct referral to the Pediatric Clinic"
elif age_patient > 80:
    result = "PRIORITY: Elderly patients - Wheelchair assistance, transfer to Geriatric clinic."
else:
    result = "ROUTE EXAMINATION: Please take a number and wait for your turn in the lobby."

print("---Electronic medical examination form---")
print(f"Họ và tên: {name_patient}")
print(f"Tuổi bệnh nhân: {age_patient}")
print(f"Kết quả phân luồng: {result}")