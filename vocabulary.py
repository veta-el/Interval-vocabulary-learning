# -*- coding: cp1251 -*-

import pandas as pd
import random
import time
import datetime

def revise_words (filename: str, columns: list, to_limit: int): #Filename with extension, list of columns to select words-definitions (or more), to_limit (how much words to revise or False)
    def check_date (today, date_update, status): #Say if this word needs to be revised based on the interval status
        if status == 1: #New word
            return True
        if status == 2: #Once in two days
            if (today - date_update).days >= 2:
                return True
            else:
                return False
        if status == 3: #Once in a week
            if (today - date_update).days >= 7:
                return True
            else:
                return False
        if status == 4: #Once in two weeks
            if (today - date_update).days >= 14:
                return True
            else:
                return False
        if status == 5: #Once in a month
            if (today - date_update).days >= 30:
                return True
            else:
                return False
        if status == 6: #Once in two months
            if (today - date_update).days >= 60:
                return True
            else:
                return False
        if status == 7: #Once in three months
            if (today - date_update).days >= 90:
                return True
            else:
                return False
        if status == 8: #Once in half a year
            if (today - date_update).days >= 180:
                return True
            else:
                return False
        if status == 9: #Once in a year
            if (today - date_update).days >= 365:
                return True
            else:
                return False
        if status == 10: #Learned
            return False

    today = datetime.date.today() #Get today date
    today = datetime.datetime.strptime (str(today), '%Y-%m-%d')

    try:
        data = pd.read_csv (filename) #Load vocabulary
    except FileNotFoundError:
        print ('File not found')
        return

    for column in columns:
        if column not in list(data.columns):
            print ('Wrong columns')
            return

    dates = list((data ['updated']).astype (str))
    if (dates [0]) [4] == '-': #Check the format of dates and set the right format
        dates = [datetime.datetime.strptime (date, '%Y-%m-%d') for date in dates]
    else:
        dates = [datetime.datetime.strptime (date, '%d.%m.%Y') for date in dates]
    data ['updated'] = dates

    data = (data.sample (frac=1)).reset_index (drop=True) #Mix words

    #Counters for statistics
    good = 0
    wrong = 0

    limiter = 0
    for i in range (0, data.shape [0]): #Find how many words can be revised
        if check_date (today, data.at [i, 'updated'], data.at [i, 'status']):
            limiter += 1
    if to_limit:
        if to_limit < limiter:
            limiter = to_limit

    for i in range (0, data.shape [0]): #Main process
        if limiter == 0:
            break
        if not check_date (today, data.at [i, 'updated'], data.at [i, 'status']):
            continue
        data.at [i, 'updated'] = today #Update the date of current word revision
        random.seed(time.localtime())
        unknown_column = random.choice(columns)
        print (unknown_column + ': '+data.at [i, unknown_column])
        current_mark = data.at [i, 'status']
        for c in columns:
            if c != unknown_column: #Checking logic
                print (c + ': ')
                answer = input ()
                if answer == data.at [i, c]:
                    good += 1
                    print ('Good!          Words to answer: '+str (limiter))
                    if current_mark != 10: #Update word status
                        data.at [i, 'status'] = current_mark + 1
                else:
                    wrong += 1
                    print ('Wrong - '+data.at [i, c]+'          Words to answer: '+str (limiter))
                    data.at [i, 'status'] = 1 #Reset status if wrong
        limiter -= 1
    print ('Result: Good - '+str (good)+' , Wrong - '+str (wrong))
    data = data.sort_values('original_index')
    data = data.reset_index (drop = True)
    data.to_csv (filename) #Update the original file

if __name__ == '__main__':
    filename = input ('Path to the file: ')
    columns = (input ('Columns to revise (space separated): ')).split (' ')
    to_limit = int(input ('Limit of words (0 if no limit): '))
    revise_words (filename, columns, to_limit)