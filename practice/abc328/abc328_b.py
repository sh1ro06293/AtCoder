n = int(input())
d = list(map(int, input().split()))

zorome = 0

for i in range(n):
    month = i + 1
    if 10 <= month:
        month_li = list(str(month))
        for j in range(len(month_li)-1):
            if month_li[j] == month_li[j+1]:
                month_zorome = True
            else:
                month_zorome = False
                break       
    else:
        month_zorome = True
    
    if month_zorome:
        for k in range(d[i]):
            day = k + 1
            if 10 <= day:
                day_li = list(str(day))
                for l in range(len(day_li)-1):
                    if day_li[l] == day_li[l+1]:
                        day_zorome = True
                    else:
                        day_zorome = False
                        break
            else:
                day_zorome = True

            if day_zorome:
                if 10 <= month and 10 <= day:
                    if month_li[0] == day_li[0]:
                        zorome += 1
                elif 10 <= day:
                    if month == int(day_li[0]):
                        zorome += 1 

                elif 10 <= month:
                     if int(month_li[0]) == day:
                        zorome += 1
                else: 
                    if month == day:
                        zorome += 1
                    

print(zorome)