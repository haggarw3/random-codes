import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('ironhackLisa-8f98c911811f.json', scope)
client = gspread.authorize(credentials)
sheetA = client.open('Copy of EA MIA DB').worksheet('PI_CALCULATOR')
sheetB = client.open('Copy of EA MIA DB').worksheet('WD_technical')
data1 = pd.DataFrame(sheetA.get_all_records())
data2 = pd.DataFrame(sheetB.get_all_records())
data2 = data2[data2['Category'] == 'Pass'].reset_index(drop=True)
temp = data2[['Name', 'E-mail']].to_dict(orient='records')
data1_names = list(data1['Name'])
rowNum = len(data1)
for diction in temp:
    if diction['Name'] not in data1_names:
        rowNum += 1
        sheetA.insert_row([diction['Name'], diction['E-mail']], rowNum)
