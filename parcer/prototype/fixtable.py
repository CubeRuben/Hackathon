import csv
import os

files = os.listdir("converted")

for filename in files:
    with open('fixed/fixed-' + filename, 'w', newline='') as fixfile:
        print(f"Fixing {filename}")

        csvwriter = csv.writer(fixfile)
        with open("converted\\" + filename, 'r') as file:
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
                dotWas = False
                
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
            
            print(f"Is table mirrored? {mirrored}")

        print(f"{filename} fixed!")