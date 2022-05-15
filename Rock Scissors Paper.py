import random
f = open("/content/가위바위보.txt", 'w')

count_L = 0
count_W = 0
count_D = 0

while True:
  i = random.randint(1,3)
  if i == 1:
    com = '가위'
  elif i == 2:
    com = '바위'
  else:
    com = '보'
  inp = input("가위, 바위, 보 중 하나를 입력해 주세요.")
  print("컴퓨터는%s을(를) 냈습니다."%com)
  print("사람은 %s을(를) 냈습니다."%inp)

  if com == inp:
    print("비겼습니다.")
    count_D = count_D + 1
  else:
    if com == "바위":
      if inp == "가위":
        print("사람이 졌습니다.")
        count_L = count_W + 1
    elif inp == "보":
      print("사람이 이겼습니다.")
      count_W = count_W + 1

    elif com == "가위":
      if inp == "보":
        print("사람이 졌습니다")
      elif inp == "바위":
        print("사람이 이겼습니다.")
        count_W = count_W + 1

    elif com == "보":
      if inp == "바위":
        print("사람이 졌습니다.")
      count_L = count_L + 1
    elif inp == "가위":
        print("사람이 이겼습니다.")
    count_W = count_W + 1
    if count_W == 5:
      print("사람이 5회 이겼습니다.")
      print("총 %d번 비겼고, %d번 졌습니다."%(count_D,count_L))
      f.write("총 %d번 비겼고, %d번 졌습니다."%(count_D,count_L))
      break
f.close()
