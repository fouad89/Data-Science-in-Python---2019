## Dependencies & imports
import pandas as pd 
import datetime as dt 

'''
the csv file trackin1.csv contains a table with date index & 3 columnes ['Start Time','End Time','Total Time (min)']
this program would add a line for each start
Date		Start Time	End Time	Total Time (mins)
12/01/2019	16:44:29	21:03:05	258

to start: answer "Y" to the question


'''
previous = pd.read_csv("trackin1.csv",index_col='Date')
#print(previous)
today = dt.date.today().strftime('%d/%m/%Y')
start_input = input('would you like to start? Y/n')

if start_input.lower()=='y':
	start_time = dt.datetime.now()
	fstart_time=start_time.time().strftime('%H:%M:%S')
	pass

else: 
	exit() 


end_input = input('When done, enter "end" ')

if end_input.lower()=='end':
	end_time = dt.datetime.now()
	fend_time = end_time.time().strftime('%H:%M:%S')
else:
	end_input = input('When done, enter "end" ')


total_time = int((end_time-start_time).total_seconds()/60)

previous = previous.append(pd.Series([fstart_time,fend_time,total_time],index=previous.columns,name=today))

print("Here are the last 5 records {}\n{}".format(previous.columns,previous.tail(5)))
previous.to_csv('trackin1.csv')


print('Your total number of hours: {0:.2f} hours'.format((previous['Total Time (mins)'].sum())/60))


