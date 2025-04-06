for i in range(1,int(input())+1):
  b=input().split(r'"')
  if "Cut" in b[2]:
    c=int(b[1].find(b[-2]))
    if c==-1:
      print(f'Command #{i}: "{b[1]}"')
    else:
      print(f'Command #{i}: "{b[1][0:c]+b[1][c+len(b[-2]):]}"')
  elif "Append" in b[2]:
    print(f'Command #{i}: "{b[1]+b[-2]}"')
  elif "Insert" in b[2]:
    print(f'Command #{i}: "{b[1][0:int(b[2][8:])-1]+b[-2]+b[1][int(b[2][8:])-1:]}"')
  else:#replace
    c=int(b[1].find(b[-4]))
    if c==-1:
      print(f'Command #{i}: "{b[1]}"')
    else:
      print(f'Command #{i}: "{b[1][0:c]+b[-2]+b[1][c+int(len(b[-4])):]}"')
#2024-05-10 19:42:17
#https://judge.hkoi.org/submission/1162516/details?sharing=9FDNolxtzmCe7MLXVlJnt2wRM
#評測結果
#子任務	測試	結果	執行時間	記憶體	分數
#1	1	正確	0.016 s	8.367 MB	100.000
#1	2	正確	0.014 s	8.316 MB	100.000
#1	3	正確	0.014 s	8.398 MB	100.000
#1	4	正確	0.014 s	8.285 MB	100.000
#1	5	正確	0.013 s	8.453 MB	100.000
#1	6	正確	0.014 s	8.293 MB	100.000
#1	7	正確	0.014 s	8.398 MB	100.000
#1	8	正確	0.059 s	8.270 MB	100.000
