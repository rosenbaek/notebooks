from ast import arg
import webget
import csv
import argparse

def print_file_content(file):
    with open(file) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        
        for row in reader:
            print('Row #' + str(reader.line_num) + ' ' + str(row))
             # as the file is quite big...
            if reader.line_num > 50:
                break


def write_list_to_file(output_file,*lst):
    with open(output_file, 'w', encoding='UTF8') as output:
        output_writer = csv.writer(output)
        for item in lst:
            if type(item) == list or type(item) == tuple:
                for i in item:
                    print(i)
                    output_writer.writerow(i)
            else:
                print(item)
                output_writer.writerow(item)

def read_csv(input_file):
    with open(input_file) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        list = []
        for row in reader:
            list.append(row)
            # as the file is quite big...
            if reader.line_num > 50:
                break
        print(list)
        return list    

if __name__ == '__main__':
    parser= argparse.ArgumentParser(description='A module that can read, write and print csv files')
    parser.add_argument('path', help='URL Path of the csv file')
    parser.add_argument('--file', help='if given will write the content to file_name or otherwise will print it to the console')
    argument = parser.parse_args()
    # Download the file in case we do not have it already
    #url = 'https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2020-financial-year-provisional/Download-data/annual-enterprise-survey-2020-financial-year-provisional-csv.csv' 
    downloadedFile = webget.download(argument.path)
    myList = ["this", "is", "my", "list"]
    myTuple = ("this", "is", "my", "tuple")
    #print_file_content(downloadedFile)
    #write_list_to_file("list_output.csv",myList)
    #write_list_to_file("tuple_output.csv",myTuple)
    #write_list_to_file("arbitary_output.csv","this", "is", "arbitary", "strings")
    #read_csv("annual-enterprise-survey-2020-financial-year-provisional-csv.csv")

    if argument.file is not None:
        write_list_to_file(argument.file, read_csv(downloadedFile))
    else:
        print_file_content(downloadedFile)