def isYearLeap(year):
	if year%4==0:
			if year%400!=0 and year%100==0:
				return False
			return True
	else:
		return False

month_with_31days = [1,3,5,7,8,10,12]
month_with_30days = [4,6,9,11]

def daysInMonth(year, month):
	if month in month_with_31days:
		return 31
	elif month in month_with_30days:
		return 30
	elif month == 2 and isYearLeap(year)==True:
		return 29
	elif month == 2 and isYearLeap(year)==False:
		return 28
	#if wrong month is provided returns None
	else:
		return None

def dayOfYear(year, month, day):
	#prevents incorrect month input using previous function
	if daysInMonth(year,month)==None:
		return None
	#prevents incorrect day input checking if there is such day in given month:
	if day<=0 or day > daysInMonth(year,month):
		return None
	#calculations:
	sum_of_days=0
	#for loop that adds all full months
	for m in range(month-1):
		sum_of_days += daysInMonth(year,m+1)
	#adding days from last month
	sum_of_days = sum_of_days + day
	return sum_of_days

print(dayOfYear(2020, 4, 7))

