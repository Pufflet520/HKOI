n = int(input())
c = 0
for x in range(1,n+1):
  a = input().split('"')
  print('Command #'+str(x)+': "',end="")
  #s = a[1].split()
  s=a[1]
  c = a[2]
  w = a[3]
  # print(s)
  #print(a[1])
  if "Cut" in c:
    q=len(w)
    if w in a[1]:
      for i in range(len(s)):
        if (i+q)>len(s):
            print(s[i:]+'"')
            break
        elif s[i:i+q]==w:
            print(s[i+q:]+'"')
            break
        else:
            print(s[i],end="")
    else:
      print(1)
      print(s+'"')
      
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
    print(a[1]+w+'"')
    

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
    print('"')
    
  elif "Replace" in c:
    q=len(a[-4])
    for i in range(len(s)):
        if (i+q)>len(s):
            print(s[i:]+'"')
            break
        elif s[i:i+q]==a[-4]:
            print(a[-2]+s[i+q:]+'"')
            break
        else:
            print(s[i],end="")
# 評測結果
# 子任務	測試	結果	執行時間	記憶體	分數
# 1	1	答案錯誤	0.014 s	8.508 MB	
# 1	2	答案錯誤	0.013 s	8.469 MB	
# 1	3	答案錯誤	0.014 s	8.434 MB	
# 1	4	答案錯誤	0.014 s	8.375 MB	
# 1	5	答案錯誤	0.014 s	8.422 MB	
# 1	6	正確	0.014 s	8.449 MB	100.000
# 1	7	答案錯誤	0.014 s	8.504 MB	
# 1	8	答案錯誤	0.111 s	8.391 MB	
# https://judge.hkoi.org/submission/1193015/details?sharing=TSHzsr2JlfnrjA1LFhDsgqB1DKg
# 2024-07-22 10:02:47
