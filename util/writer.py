import csv

class Writer(object):

    def toCSV(self, fileName, data):
        with open(fileName, "w") as csvFile:
            writer = csv.writer(csvFile)

            for hashtag in data:
                row = [hashtag[0], hashtag[1]]
                writer.writerow(row)

        csvFile.close()

    