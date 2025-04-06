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
