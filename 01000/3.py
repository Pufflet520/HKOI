for i in range(1,int(input())+1):
  b=input().split(r'"')
  a=b[2]
  if "Cut" in a:
    c=int(b[1].find(b[-2]))
    if c==-1:
      print(f'Command #{i}: "{b[1]}"')
    else:
      print(f'Command #{i}: "{b[1][0:c]+b[1][c+len(b[-2]):]}"')
  elif "Append" in a:
    print(f'Command #{i}: "{b[1]+b[-2]}"')
  elif "Insert" in a:
    print(f'Command #{i}: "{b[1][0:int(a[8:])-1]+b[-2]+b[1][int(a[8:])-1:]}"')
  else:#replace
    c=int(b[1].find(b[-4]))
    if c==-1:
      print(f'Command #{i}: "{b[1]}"')
    else:
      print(f'Command #{i}: "{b[1][0:c]+b[-2]+b[1][c+int(len(b[-4])):]}"')
#評測結果 100.000
#子任務	測試	結果	執行時間	記憶體	分數
#1	1	正確	0.013 s	8.383 MB	100.000
#1	2	正確	0.013 s	8.406 MB	100.000
#1	3	正確	0.013 s	8.371 MB	100.000
#1	4	正確	0.013 s	8.461 MB	100.000
#1	5	正確	0.013 s	8.309 MB	100.000
#1	6	正確	0.013 s	8.371 MB	100.000
#1	7	正確	0.013 s	8.457 MB	100.000
#1	8	正確	0.055 s	8.461 MB	100.000
