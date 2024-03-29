"""
1. 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

    低于18.5：过轻
    18.5-25：正常
    25-28：过重
    28-32：肥胖
    高于32：严重肥胖
"""

def BMIProgramme(weight, height):
    BMI = weight / (height * 2)
    if BMI < 18.5:
        s = 'underweight'
    elif 18.5 < BMI < 25:
        s = 'standard'
    elif 25 < BMI < 28:
        s = 'overweight'
    elif 28 < BMI < 32:
        s = 'obese'
    elif BMI > 32:
        s = 'heavily obese'
    else:
        s = 'YOU MUST BE KIDDING ME!'
    return s

print(BMIProgramme(80.5, 1.75))



