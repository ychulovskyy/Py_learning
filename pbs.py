import csv

nmr = 'boB'
lst_U = []
dict = {}

with open('pb.csv', 'r') as fl:
    rds = csv.DictReader(fl)
    for dict in rds:  # All readings from the file go to Dictionary 'dict'
        l_fname = dict.get('f_name')
        l_lname = dict.get('l_name')
        l_number = dict.get('number')
        for i in range(len(l_fname) - 1):  # The first name analysis
            if l_fname[i:i + len(nmr)].lower() == nmr.lower() and not l_number in lst_U:
                lst_U.append(l_number)  # adding the number to lst_U  if we found something
        for i in range(len(l_lname) - 1):  # The second name analysis
            if l_lname[i:i + len(nmr)].lower() == nmr.lower() and not l_number in lst_U:
                lst_U.append(l_number)  # adding the number to lst_U if we found something

print('We are searching...', nmr)
print('_________________')
print('We found...')

with open('pb.csv', 'r') as fl:
    rds = csv.DictReader(fl)
    for dict in rds:  # comparing file-data and the list of found numbers
        if dict.get('number') in lst_U:
            print('Name:', dict.get('f_name'), dict.get('l_name'), '     Phone number:', dict.get('number'))
if lst_U == []: print('Nothing')
