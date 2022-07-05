#mcat and gpa data: https://www.aamc.org/media/6091/download 
#race data: https://www.shemmassianconsulting.com/blog/medical-school-acceptance-rates-by-race#part-2-medical-school-acceptance-rates-by-race
#gender data: https://www.aamc.org/media/9576/download?attachment

total = 164428.0
accepted = 67158.0
rate = accepted/total

def mcatGpaFunc(m, gp):
    if(gp > 3.79):
        if(m>517):
            return .842
        if(m>=514):
            return .775
        if(m>=510):
            return .691
        if(m>=506):
            return .550
        if(m>=502):
            return .402
        if(m>=498):
            return .283
        if(m>=494):
            return .171
        if(m>=490):
            return .055
        if(m>=486):
            return .021
        else:
            return .012
    if(gp >= 3.60):
        if(m>517):
            return .743
        if(m>=514):
            return .689
        if(m>=510):
            return .584
        if(m>=506):
            return .417
        if(m>=502):
            return .298
        if(m>=498):
            return .213
        if(m>=494):
            return .115
        if(m>=490):
            return .045
        if(m>=486):
            return .008
        else:
            return .011
    if(gp >= 3.40):
        if(m>517):
            return .643
        if(m>=514):
            return .573
        if(m>=510):
            return .475
        if(m>=506):
            return .336
        if(m>=502):
            return .245
        if(m>=498):
            return .176
        if(m>=494):
            return .096
        if(m>=490):
            return .025
        if(m>=486):
            return .012
        else:
            return .013
    if(gp >= 3.20):
        if(m>517):
            return .550
        if(m>=514):
            return .499
        if(m>=510):
            return .396
        if(m>=506):
            return .295
        if(m>=502):
            return .222
        if(m>=498):
            return .147
        if(m>=494):
            return .073
        if(m>=490):
            return .021
        if(m>=486):
            return .010
        else:
            return .004
    if(gp >= 3.00):
        if(m>517):
            return .526
        if(m>=514):
            return .424
        if(m>=510):
            return .321
        if(m>=506):
            return .263
        if(m>=502):
            return .207
        if(m>=498):
            return .153
        if(m>=494):
            return .067
        if(m>=490):
            return .016
        if(m>=486):
            return .005
        else:
            return .003
    if(gp >= 2.80):
        if(m>517):
            return .467
        if(m>=514):
            return .324
        if(m>=510):
            return .289
        if(m>=506):
            return .228
        if(m>=502):
            return .176
        if(m>=498):
            return .112
        if(m>=494):
            return .037
        if(m>=490):
            return .015
        if(m>=486):
            return .009
        else:
            return .004
    if(gp >= 2.60):
        if(m>517):
            return .280
        if(m>=514):
            return .305
        if(m>=510):
            return .240
        if(m>=506):
            return .233
        if(m>=502):
            return .165
        if(m>=498):
            return .099
        if(m>=494):
            return .040
        if(m>=490):
            return .009
        if(m>=486):
            return .012
        else:
            return .000
    if(gp >= 2.40):
        if(m>517):
            return .300
        if(m>=514):
            return .235
        if(m>=510):
            return .184
        if(m>=506):
            return .247
        if(m>=502):
            return .069
        if(m>=498):
            return .047
        if(m>=494):
            return .033
        if(m>=490):
            return .012
        else:
            return .000
    if(gp >= 2.20):
        if(m>517):
            return .000
        if(m>=514):
            return .000
        if(m>=510):
            return .167
        if(m>=506):
            return .242
        if(m>=502):
            return .083
        if(m>=498):
            return .104
        if(m>=494):
            return .046
        else:
            return .000
    if(gp >= 2.00):
        return .000
    else:
        if(m>485 and m<490):
            return .077
        else:
            return .000

def raceFunc(r):
    if(r == 1):
        return .44
    if(r == 2):
        return .40
    if(r == 3):
        return .36
    if(r == 4):
        return .41
    if(r == 5):
        return .34
    if(r == 6):
        return .39
    else:
        return .32

def genderFunc(ge):
    #men
    if(ge == 1): 
        return 10537.0/26948.0
    #women
    else:
        return 13152.0/35438.0

mcat = input('Input MCAT: \n')
mcat = int(mcat)
while(mcat <472 or mcat >528):
    mcat = input('MCAT was not a valid score, please input again: \n')
    mcat = int(mcat)

gpa = input('Input GPA: \n')
gpa = float(gpa)
while(gpa <0.0 or gpa >4.0):
    gpa = input('GPA was not a valid score, please input again: \n')
    gpa = float(gpa)

race = input('Race choices are listed below: \n american indian(1) \n asian(2) \n black(3) \n hispanic(4) \n hawaiin(5)\n white(6) \n other(7) \n')
race = int(race)
while(race <1 or race > 7):
    race = input('Race choice was not valid, please input again: \n american indian(1) \n asian(2) \n black(3) \n hispanic(4) \n hawaiin(5)\n white(6) \n other(7) \n')
    race = int(race)

gender = input('Gender choices are listed below: \n male(1) \n female(2)')
gender = int(gender)
while(gender<1 or gender>2):
    gender = input('Gender choice was not valid, please input again: \n male(1) \n female(2)')
    gender = int(gender)

mP = mcatGpaFunc(mcat, gpa) 
rP = raceFunc(race)
gP = genderFunc(gender)
print("--------------------| Results |--------------------")
print("National acceptance rate: " + str(round((rate *100),1)) + "%")
print("\nAceptance rate based on: ")
print("Inputted MCAT and GPA: " + str(round((mP*100),1)) + "%")
print("Inputted Race: " + str(round((rP*100),1)) + "%")
print("Inputted Gender: " + str(round((gP*100),1)) + "%")