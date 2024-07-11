from os import wait
import time
print ("หากคุณเป็นเพศชาย โปรดกด 1")
time.sleep(1)
print ("หากคุณเป็นเพศหญิง โปรดกด 2")
Gender = int(input("เพศของคุณ คือ : "))
Age = int(input("อายุของคุณ คือ : "))
Weight = int(input("น้ำหนักของคุณ (kg) คือ : "))
Hight = int(input("ส่วนสูงของคุณ (cm) คือ : "))
Hight_m = Hight/100
BMI = Weight/(Hight_m*Hight_m)

print ("พฤติกรรมการบริโภคของหวาน") ##1
time.sleep(1)
print ("เป็นประจำ โปรดกด 3")
print ("เป็นบางครั้ง โปรดกด 2")
print ("นานทีๆ โปรดกด 1")
Sweet = int(input("พฤติกรรมการบริโภคหวานของคุณคือ : "))

print ("พฤติกรรมการบริโภคของมัน/ทอด") ##2
time.sleep(1)
print ("เป็นประจำ โปรดกด 3")
print ("เป็นบางครั้ง โปรดกด 2")
print ("นานทีๆ โปรดกด 1")
Fried = int(input("พฤติกรรมการบริโภคของมัน/ทอด"))

print ("พฤติกรรมการบริโภคเครื่องดื่มแอลกอฮอล์") ##3
time.sleep(1)
print ("เป็นประจำ โปรดกด 4")
print ("เป็นบางครั้ง โปรดกด 3")
print ("นานทีๆ โปรดกด 2")
print ("ไม่เคย โปรดกด 1")
Drinks = int(input("พฤติกรรมการบริโภคเครื่องดื่มแอลกอฮอล์ของคุณคือ : "))

print ("พฤติกรรมการสูบบุหรี่") ##4
time.sleep(1)
print ("เป็นประจำ โปรดกด 4")
print ("เป็นบางครั้ง โปรดกด 3")
print ("นานทีๆ โปรดกด 2")
print ("ไม่เคย โปรดกด 1")
Smoke = int(input("พฤติกรรมการสูบบุหรี่ของคุณคือ : "))

print ("พฤติกรรมการออกกำลังกาย") ##5
time.sleep(1)
print ("เป็นประจำ โปรดกด 3")
print ("เป็นบางครั้ง โปรดกด 2")
print ("นานทีๆ โปรดกด 1")
Ex = int(input("พฤติกรรมการออกกำลังกายของคุณคือ : "))

if (Gender == 1) : Data_Gender = 1
else : Data_Gender = 2

if (Age >=60) : Data_Age = 5
elif (Age >=50 and Age < 60) : Data_Age = 4
elif (Age >=40 and Age < 50) : Data_Age = 3
elif (Age >=30 and Age < 40) : Data_Age = 2
elif (Age <30 ) : Data_Age = 1

if (BMI >30) : Data_BMI = 4
elif (BMI >=25 and BMI <30) : Data_BMI = 3
elif (BMI >=23 and BMI <25) : Data_BMI = 2
elif (BMI >=18.50 and BMI <23) : Data_BMI = 0
elif (BMI <18.50) : Data_BMI = 1

if (Sweet == 3) : Data_Sweet = 3
elif (Sweet == 2) : Data_Sweet = 2
elif (Sweet == 1) : Data_Sweet = 1

if (Fried == 3) : Data_Fried = 3
elif (Fried == 2) : Data_Fried = 2
elif (Fried == 1) : Data_Fried = 1

if (Drinks == 4) : Data_Drinks = 3
elif (Drinks == 3) : Data_Drinks = 2
elif (Drinks == 2) : Data_Drinks = 1
elif (Drinks == 1) : Data_Drinks = 0

if (Smoke == 4) : Data_Smoke = 3
elif (Smoke == 3) : Data_Smoke = 2
elif (Smoke == 2) : Data_Smoke = 1
elif (Smoke == 1) : Data_Smoke = 0

if (Ex == 3) : Data_Ex = 1
elif (Ex == 2) : Data_Ex = 2
elif (Ex == 1) : Data_Ex = 3

Data = int(Data_Gender + Data_Age + Data_BMI + Data_Sweet + Data_Fried + Data_Drinks + Data_Smoke + Data_Ex)

if (Data >= 21 and Data <=26) :
  print("ความเสี่ยงสูงมาก")
  time.sleep(1.5)
  print("ควบคุมอาหารและออกกำลังกายสม่ำเสมอ ควบคุมน้ำหนักให้อยู่ในเกณฑ์ที่เหมาะสม ตรวจวัดความดันโลหิต ระดับน้ำตาลในเลือด ควรประเมินความเสี่ยงซ้ำทุกๆ 1 ปี")
elif (Data >=16 and Data <=20) :
  print("ความเสี่ยงสูง")
  time.sleep(1.5)
  print("ควบคุมอาหารและออกกำลังกายสม่ำเสมอ ควบคุมน้ำหนักให้อยู่ในเกณฑ์ที่เหมาะสม ตรวจวัดความดันโลหิต ระดับน้ำตาลในเลือด ควรประเมินความเสี่ยงซ้ำทุกๆ 1-3 ปี")
elif (Data >=11 and Data <=15) :
  print("ความเสี่ยงปานกลาง")
  time.sleep(1.5)
  print("ควบคุมอาหารและออกกำลังกายสม่ำเสมอ ควบคุมน้ำหนักให้อยู่ในเกณฑ์ที่เหมาะสม ตรวจวัดความดันโลหิต ควรประเมินความเสี่ยงซ้ำทุกๆ 3 ปี")
elif(Data >=6 and Data <=10) :
  print("ความเสี่ยงน้อย")
  time.sleep(1.5)
  print("ควบคุมอาหารและออกกำลังกายสม่ำเสมอ ควบคุมน้ำหนักให้อยู่ในเกณฑ์ที่เหมาะสม ตรวจวัดความดันโลหิต ควรประเมินความเสี่ยงซ้ำทุกๆ 3 ปี")