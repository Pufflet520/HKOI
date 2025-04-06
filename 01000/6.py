n = int(input())
c = 0
for x in range(1,n+1):
  a = input().split('"')
  print('Command #'+str(x)+': "',end="")
  s = a[1].split()
  c = a[2]
  w = a[3]
  # print(s)
  #print(a[1])
  if "Cut" in c:
    if w in a[1]:
      for i in range(len(a[1])-len(w)):
        if a[1][i:len(w)+i] == w:
          print(a[1][len(w)+i:],end='"')
          break
        print(a[1][i],end="")
        
    else:
      print(a[1]+'"',end="")
      
    # print('"',end="")
    
    # if s[-1] != w.split()[0]:
    #   for i in range(len(s)):
    #     if i != len(s)-1:
    #       if s[i] != w.split()[0]:
    #         print(s[i],end=" ")
    #       else:
    #         if c != 0:
    #           print(s[i],end=" ")
    #           c = 1
    #   print(s[-1],end='"')
    # else:
    #   for i in range(len(s)):
    #     if i != len(s)-2:
    #       if s[i] != w.split()[0]:
    #         print(s[i],end=" ")
    #   print(s[-2],end='"')
      
  elif "Append" in c:
    print(a[1]+w+'"',end="")
    

    # s.append(w.split()[0])
    # for i in range(len(s)):
    #   if i != len(s)-1:
    #     print(s[i],end=" ")
    # print(s[-1],end='"')
    
  elif "Insert" in c:
    for i in range(len(a[1])):
      if i+1 == int(c.split()[1]):
        print(w,end="")
      print(a[1][i],end="")
    print('"',end='')
    
  elif "Replace" in c:
    # for i in range(len(a[1])-len(w)):
    #   if a[1][i:len(w)+i] == w:
    #     print(a[5],end="")
    #     print(a[1][len(w)+i:],end='"')
    #     break
    #   print(a[1][i],end="")
        



    
    for i in range(len(s)):
      if i != len(s)-1:
        if s[i] != w:
          print(s[i],end=" ")
        else:
          print(a[5],end=" ")
    print(s[-1],end='"')

  print()
#   評測結果
# 子任務	測試	結果	執行時間	記憶體	分數
# 1	1	正確	0.014 s	8.352 MB	100.000
# 1	2	正確	0.012 s	8.332 MB	100.000
# 1	3	答案錯誤	0.013 s	8.414 MB	
# 1	4	執行錯誤	0.012 s	8.328 MB	
# 1	5	答案錯誤	0.012 s	8.383 MB	
# 1	6	正確	0.013 s	8.516 MB	100.000
# 1	7	執行錯誤	0.012 s	8.426 MB	
# 1	8	答案錯誤	0.089 s	8.434 MB
# https://judge.hkoi.org/submission/1192922/details?sharing=D3Vwe94Ud8bA3r3SNZoNWYav8uM
# 2024-07-21 17:59:47
