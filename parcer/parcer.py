import tabula
import requests
import csv
import os

class Parcer:

    def __init__(self, convertedPrefixPath, fixPrefixPath, combinedPrefixPath):
        self.convertedPrefixPath = convertedPrefixPath
        self.fixPrefixPath = fixPrefixPath
        self.combinedPrefixPath = combinedPrefixPath

    def setReportLocation(self, path):
        self.reportPath = path

    def downloadReport(self, url, savePath): 

        print("Downloading file...")

        fileDownload = requests.get(url)

        file = open(savePath, 'wb')
        file.write(fileDownload.content)
        file.close()

        self.setReportLocation(savePath)

        print("Download complete")

    def getTableFromReportInCSV(self, page, coords, csvFile):
        print(f"Converting page {page}")
        tabula.convert_into(self.reportPath, self.convertedPrefixPath + csvFile, output_format="csv", guess=False, pages=page, stream=True, area=[83.589, 22.136, 659.134, 515.083], columns=coords)
        print(f"Page {page} converted!")

    def fixCSV(self, fileToFix):
        with open(self.fixPrefixPath + fileToFix, 'w', newline='') as fixfile:
            print(f"Fixing {fileToFix}")

            csvwriter = csv.writer(fixfile)
            with open(self.convertedPrefixPath + fileToFix, 'r') as file:
                csvreader = csv.reader(file)
                additionalName = ''

                skipUntilNumbers = True

                mirrored = True

                for row in csvreader:
                    if skipUntilNumbers:
                        for el in row:
                            if any(i.isdigit() for i in el):
                                skipUntilNumbers = False
                                break
                            
                        if not skipUntilNumbers:
                            if any(el.isdigit() for el in row[len(row) - 1]):
                                mirrored = False

                        if skipUntilNumbers:
                            continue

                    if '1)' in row[0]:
                        break

                    numbers = ''

                    if not mirrored:
                        numbers = row[1:len(row)]
                    else: 
                        numbers = row[0:len(row) - 1]

                    #numbers = ' '.join(numbers).replace('"', ' ').replace(',.', '').replace('...2)', '0,0').replace('..2)', '0,0').replace('...', '0,0').replace('  ', ' ').replace('-', '0,0').replace('–', '0,0')

                    newNumbers = []

                    for el in numbers:
                        if el != '':
                            newNumbers.append(float(el.replace('...2)', '0,0').replace('..2)', '0,0').replace('2)', '0,0').replace('-', '0,0').replace('–', '0,0').replace('...', '0,0').replace(' ', '').replace(',', '.')))

                    if len(newNumbers) != 0:
                        if mirrored:
                            csvwriter.writerow(newNumbers)
                        else:
                            csvwriter.writerow([additionalName + row[0]] + newNumbers)
                        additionalName = ''
                    else:
                        additionalName = row[0] + ' '

                print(f"DEBUG - Is table mirrored? {mirrored}")

            print(f"{fileToFix} fixed!")

    def combineMirrored(self, file1, file2, outfile):
        print(f"Miror combine of {file1} and {file2}")
        with open(self.combinedPrefixPath + outfile, 'w', newline='') as writeFile:
            with open(self.fixPrefixPath + file1, 'r') as fileFirst:
                with open(self.fixPrefixPath + file2, 'r') as fileSecond:
                    listFirst = list(csv.reader(fileFirst))
                    listSecond = list(csv.reader(fileSecond))

                    writer = csv.writer(writeFile)

                    for i in range(len(listFirst)):
                        writer.writerow(list(listFirst[i] + listSecond[i]))

    def combineRegular(self, file1, file2, outfile):
        print(f"Regular combine of {file1} and {file2}")
        with open(self.combinedPrefixPath + outfile, 'w', newline='') as writeFile:
            with open(self.combinedPrefixPath + file1, 'r') as fileFirst:
                with open(self.combinedPrefixPath + file2, 'r') as fileSecond:
                    readerFirst = csv.reader(fileFirst)
                    readerSecond = csv.reader(fileSecond)

                    writer = csv.writer(writeFile)

                    for el in readerFirst:
                        writer.writerow(el)

                    for el in readerSecond:
                        writer.writerow(el)