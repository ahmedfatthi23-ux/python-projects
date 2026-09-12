print('====BMI AND BODYFAT CALCULATER ====')

height = int(input('Enter your height(cm):'))
weight = int(input('Enter your weight(kg):'))

while True:
    neck = int(input('Enter your neck(cm):'))
    waist = int(input('Enter your waist(cm):'))
    if neck > waist:
        print("try again")
    else:
        break

heightm = height / 100
height2 = heightm * heightm
bmi = round(weight / height2, 2)

wn = waist - neck
import math

wnlog = math.log10(wn)
hlog = math.log10(height)

wncon = 0.19077 * wnlog
hcon = 0.15456 * hlog

wnbd = 1.0324 - wncon
bodydensity = wnbd + hcon

z = 495 / bodydensity
bodyfat = round(z - 450, 2)

print('====RESULTS====')
print('your bmi is:',bmi)
print('your body fat percentage is:',bodyfat)