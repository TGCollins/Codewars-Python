# If, else Method
def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) / 3 
    if score < 60: 
       return 'F' 
    elif score < 70: 
       return 'D' 
    elif score < 80: 
       return 'C' 
    elif score < 90: 
       return 'B' 
    else :
       return 'A'
 
# Dictionary Method

def get_grade(s1,s2,s3):
    grades = {10: 'A',9: 'A',8: 'B',7: 'C',6: 'D',}
    res = (s1+s2+s3) / 3
    return grades.get(res // 10, 'F')
