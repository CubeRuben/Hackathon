import csv

def combineMirrored(file1, file2, outfile):
    print(f"Miror combine of {file1} and {file2}")
    with open(outfile, 'w', newline='') as writeFile:
        with open(file1, 'r') as fileFirst:
            with open(file2, 'r') as fileSecond:
                listFirst = list(csv.reader(fileFirst))
                listSecond = list(csv.reader(fileSecond))

                writer = csv.writer(writeFile)

                for i in range(len(listFirst)):
                    writer.writerow(list(listFirst[i] + listSecond[i]))

def combineRegular(file1, file2, outfile):
    print(f"Regular combine of {file1} and {file2}")
    with open(outfile, 'w', newline='') as writeFile:
        with open(file1, 'r') as fileFirst:
            with open(file2, 'r') as fileSecond:
                readerFirst = csv.reader(fileFirst)
                readerSecond = csv.reader(fileSecond)

                writer = csv.writer(writeFile)

                for el in readerFirst:
                    writer.writerow(el)

                for el in readerSecond:
                    writer.writerow(el)

combineMirrored('fixed/fixed-table-page525.csv', 'fixed/fixed-table-page526.csv', 'temp1.csv')
combineMirrored('fixed/fixed-table-page527.csv', 'fixed/fixed-table-page528.csv', 'temp2.csv')
combineRegular('temp1.csv', 'temp2.csv', 'combined/income.csv')

combineMirrored('fixed/fixed-table-page515.csv', 'fixed/fixed-table-page516.csv', 'temp1.csv')
combineMirrored('fixed/fixed-table-page517.csv', 'fixed/fixed-table-page518.csv', 'temp2.csv')
combineRegular('temp1.csv', 'temp2.csv', 'combined/number_of_enterprises.csv')

combineMirrored('fixed/fixed-table-page463.csv', 'fixed/fixed-table-page464.csv', 'temp1.csv')
combineMirrored('fixed/fixed-table-page465.csv', 'fixed/fixed-table-page466.csv', 'temp2.csv')
combineRegular('temp1.csv', 'temp2.csv', 'combined/gdprel.csv')