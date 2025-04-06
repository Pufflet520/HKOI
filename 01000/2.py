for i in range(int(input())):
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
#2024-05-10 19:25:46
#https://judge.hkoi.org/submission/1162510/details?sharing=x7KMkJMhunFRtH5Fx0VAyPY6OU
#提交 1162510
#評測結果 12.500
#子任務	測試	結果	執行時間	記憶體	分數
#1	1	答案錯誤	0.014 s	8.352 MB	
#1	2	答案錯誤	0.014 s	8.277 MB	
#1	3	答案錯誤	0.013 s	8.242 MB	
#1	4	答案錯誤	0.013 s	8.371 MB	
#1	5	答案錯誤	0.013 s	8.297 MB	
#1	6	正確	0.013 s	8.363 MB	100.000
#1	7	答案錯誤	0.014 s	8.320 MB	
#1	8	答案錯誤	0.060 s	8.297 MB	
