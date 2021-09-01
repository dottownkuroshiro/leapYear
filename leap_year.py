# 西暦年を入力すると閏年かどうかを判定する
def leap_year_judge(year):
  if year % 400 == 0:
    return True
  elif year % 100 == 0:
    return False
  elif year % 4 == 0:
    return True
  else:
    return False

print("西暦年を半角で入力してください")
year = input()
year = int(year)
answer = leap_year_judge(year)
if answer == True:
  print(str(year)+"年は閏年です")
elif answer == False:
  print(str(year)+"年は閏年ではありません")
