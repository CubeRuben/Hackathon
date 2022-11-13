import tabula
import requests

print("Downloading file..")

fileDownload = requests.get("https://rosstat.gov.ru/storage/mediabank/Region_Pokaz_2021.pdf")

file = open("report.pdf", 'wb')
file.write(fileDownload.content)
file.close()

print("Download complete")

def convert(pages, coords):
    for page in pages:

        print(f"Converting page {page}")

        tabula.convert_into("report.pdf", f"converted/table-page{page}.csv", output_format="csv", guess=False, pages=page, stream=True, area=[83.589, 22.136, 659.134, 515.083], columns=coords)

        print(f"Page {page} converted!")

convert([463, 465], [118.611, 152.972, 189.315, 223.676, 258.698, 293.719, 328.08, 363.763, 398.124, 433.806, 468.167, 503.189])
convert([464, 466], [65.748, 104.074, 142.399, 180.725, 219.051, 256.715, 295.041, 332.706, 371.692, 406.714, 503.18])
convert([525, 527], [133.809, 170.813, 207.156, 244.16, 281.164, 318.829, 355.172, 392.837, 429.18, 466.185, 502.528])
convert([526, 528], [68.391, 108.699, 149.668, 190.637, 230.945, 272.574, 313.543, 353.851, 394.82, 503.849])
convert([515, 517], [131.827, 171.474, 207.817, 244.821, 281.825, 318.829, 355.833, 393.498, 429.841, 466.185, 505.171])
convert([516, 518], [63.766, 100.77, 137.774, 174.778, 211.782, 248.786, 285.79, 322.794, 359.798, 396.802, 503.849])