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
    c=int(b[1].find(b[-3]))
    if c==-1:
      print(f'Command #{i}: "{b[1]}"')
    else:
      print(f'Command #{i}: "{b[1][0:c+1]+b[-2]+b[1][c+int(len(b[-2]))+1:]}"')
#評測結果
#子任務	測試	結果	執行時間	記憶體	分數
#1	1	正確	0.013 s	8.355 MB	100.000
#1	2	答案錯誤	0.013 s	8.371 MB	
#1	3	答案錯誤	0.012 s	8.406 MB	
#1	4	答案錯誤	0.013 s	8.387 MB	
#1	5	答案錯誤	0.013 s	8.387 MB	
#1	6	正確	0.012 s	8.465 MB	100.000
#1	7	答案錯誤	0.013 s	8.410 MB	
#1	8	答案錯誤	0.053 s	8.391 MB	
