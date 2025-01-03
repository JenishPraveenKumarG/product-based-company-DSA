def pascal(num_row):
  first_row = 1
  rows = [first_row]

  for _ in range(1,num_row):
    row = [1]
    for i in range(1,len(rows[-1]):
      num = row[-1][i-1] + [-1][i]
      row.append(num)
    row.appemd(1)
    rows.append(row)
    
return rows

n = 5
print(pascal(n))


    
  
