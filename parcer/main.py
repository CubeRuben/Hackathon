from parcer import Parcer

def main():

    parcer = Parcer('converted/', 'fixed/', 'combined/')

    parcer.downloadReport("https://rosstat.gov.ru/storage/mediabank/Region_Pokaz_2021.pdf", "report.pdf")

    coords = [  [118.611, 152.972, 189.315, 223.676, 258.698, 293.719, 328.08, 363.763, 398.124, 433.806, 468.167, 503.189],
                [65.748, 104.074, 142.399, 180.725, 219.051, 256.715, 295.041, 332.706, 371.692, 406.714, 503.18],
                [133.809, 170.813, 207.156, 244.16, 281.164, 318.829, 355.172, 392.837, 429.18, 466.185, 502.528],
                [68.391, 108.699, 149.668, 190.637, 230.945, 272.574, 313.543, 353.851, 394.82, 503.849],
                [131.827, 171.474, 207.817, 244.821, 281.825, 318.829, 355.833, 393.498, 429.841, 466.185, 505.171],
                [63.766, 100.77, 137.774, 174.778, 211.782, 248.786, 285.79, 322.794, 359.798, 396.802, 503.849]]
    i = 0
    for page in [463, 465, 464, 466, 525, 527, 526, 528, 515, 517, 516, 518]:
        parcer.getTableFromReportInCSV(page, coords[i // 2], f'table-page{page}.csv')
        parcer.fixCSV(f'table-page{page}.csv')
        i += 1

    parcer.combineMirrored('table-page525.csv', 'table-page526.csv', 'temp1.csv')
    parcer.combineMirrored('table-page527.csv', 'table-page528.csv', 'temp2.csv')
    parcer.combineRegular('temp1.csv', 'temp2.csv', 'income.csv')

    parcer.combineMirrored('table-page515.csv', 'table-page516.csv', 'temp1.csv')
    parcer.combineMirrored('table-page517.csv', 'table-page518.csv', 'temp2.csv')
    parcer.combineRegular('temp1.csv', 'temp2.csv', 'number_of_enterprises.csv')

    parcer.combineMirrored('table-page463.csv', 'table-page464.csv', 'temp1.csv')
    parcer.combineMirrored('table-page465.csv', 'table-page466.csv', 'temp2.csv')
    parcer.combineRegular('temp1.csv', 'temp2.csv', 'gdprel.csv')

    

if __name__ == '__main__':
    main()