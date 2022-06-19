import csv
from random import randint

class Main:
    __headings = ['Id', 'Name', 'Surname', 'Date of birth', 'Age', 'City',
                  'Programming language', 'Development experience',
                  'Qualification level']

    def __init__(self):
        print('Select the desired action?:\n'
              '1. Get data by id\n'
              '2. Select the columns to export\n'
              '3. Select the entries to export\n'
              '4. Add a new entry\n'
              '5. Delete an entry\n')
        # time.sleep(5)
        try:
            action = int(input('Press the corresponding key: '))
            if action == 1:
                self.get_data()
            if action == 2:
                self.col_export()
            if action == 3:
                self.entries_exp()
            if action == 4:
                self.add_entry()
        except ValueError:
            print('Invalid action specified! Return to the main menu.')
            Main.__init__(self)

    def write_file(self, user_list, filename, mode):
        with open(f'{filename}.csv',
                  mode) as file:
            writer = csv.writer(file, lineterminator='\r')
            writer.writerows(user_list)

    def get_data(self):
        id = int(input('\nEnter the id(6 digits): '))
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            for string in reader:
                string = (';'.join(string)).split(';')
                if str(id) == string[0]:
                    print('Information about a person:')
                    for k, v in dict(zip(self.__headings[1:], string)).items():
                        print(f'{k}: {v}')

    def col_export(self):
        print('You can select one or more columns from the ones presented for export to your file:')
        for col in self.__headings:
            print(f'- {col}')
        columns = input('\nList the column names to export separated by commas: ').split(', ')
        columns = [col.capitalize() for col in columns]
        col_sort = sorted(columns, key=lambda i: self.__headings.index(i))
        user_data = []
        for col in col_sort:
            temp = []
            if col in self.__headings:
                with open('data.csv', 'r') as file:
                    reader = csv.reader(file.readlines()[1:])
                    for string in reader:
                        temp.append((';'.join(string)).split(';')[self.__headings.index(col)])
                    user_data.append(temp)
        user_data = [';'.join(list(i)).split(',') for i in zip(*user_data)]
        user_data.insert(0, ';'.join(col_sort).split(','))
        Main.write_file(self, user_data, filename='user_data', mode='w')
        print('Data export to file "user_data.csv" completed')

    def entries_exp(self):
        print('You can select one or more values of the criteria listed below to export records to your file:')
        for crit in self.__headings[5:]:
            print(f'- {crit}')
        crit_vals = input('\nList the values of the criteria for exporting the record/s, '
                          'separating them with commas: ').split(', ')
        print(crit_vals)
        record_data = []
        record_data.append([';'.join(self.__headings)])
        print(record_data)
        with open('data.csv', 'r') as file:
            reader = csv.reader(file.readlines())
            for string in reader:
                string = (';'.join(string)).split(';')
                print(string)
                if all(x in string for x in crit_vals):
                    record_data.append([';'.join(string)])
                    print(record_data)
            Main.write_file(self, record_data, filename='user_records', mode='w')
            print('Export of records to a file "user_records.csv" is completed')

    def add_entry(self):
        ent_num = int(input('How many records do you want to add? '))
        entries = []
        for ent in range(ent_num):
            print(f'\nGet ready to enter the data of the {ent + 1} record')
            temp = []
            for header in self.__headings:
                if header == 'Date of birth':
                    header = input(f'{header}, example - 09.07.1992: ')
                elif header == 'Id':
                    header = str(randint(100000, 999999))
                else:
                    header = input(f'{header}: ')
                temp.append(header)
            entries.append(([';'.join(temp)]))
            Main.write_file(self, entries, filename='data', mode='a')
            print('Adding entries to the file is completed')

    def del_entry(self):
        pass


main = Main()


