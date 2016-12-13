# -*- coding: utf-8 -*-
import re
import io

def cleanTextFile():
    # Open file to read
    textFile = open('trump.txt', 'r')
    rawText = textFile.read()
    textFile.close()

    # Begin cleaning

    # Remove speakers that aren't trump.
    cleanedText = re.sub('Unknown:[\w.,!?\’\'\"\[\]: —\-…–;”“/]*\n\n', '', rawText)
    cleanedText = re.sub('Billy Bush:[\w.,!?\’\'\"\[\]: —\-…–;”“/]*\n\n', '', cleanedText)
    cleanedText = re.sub('Bush:[\w.,!?\’\'\"\[\]: —\-…–;”“/]*\n\n', '', cleanedText)
    cleanedText = re.sub('Arianne Zucker:[\w.,!?\’\'\"\[\]: —\-…–;”“/]*\n\n', '', cleanedText)
    cleanedText = re.sub('Zucker:[\w.,!?\’\'\"\[\]: —\-…–;”“/]*\n\n', '', cleanedText)
    cleanedText = re.sub('FRED HIATT[\w.,!?\’\'\"\[\]: —\-…–;”“/]*\n\n', '', cleanedText)
    cleanedText = re.sub('STROMBERG:[\w.,!?\’\'\"\[\]: —\-…–;”“/]*\n\n', '', cleanedText)
    cleanedText = re.sub('HIATT:[\w.,!?\’\'\"\[\]: —\-…–;”“/]*\n\n', '', cleanedText)
    cleanedText = re.sub('ARMAO:[\w.,!?\’\'\"\[\]: —\-…–;”“/]*\n\n', '', cleanedText)
    cleanedText = re.sub('HOPE HICKS, TRUMP CAMPAIGN SPOKESPERSON:[\w.,!?\’\'\"\[\]: —\-…–;”“/]*\n\n', '', cleanedText)
    cleanedText = re.sub('JAMIE RILEY:[\w.,!?\’\'\"\[\]: —-…]–-*\n\n', '', cleanedText)
    cleanedText = re.sub('CHRISTINE EMBA:[\w.,!?\’\'\"\[\]: —\-…–;”“/]*\n\n', '', cleanedText)
    cleanedText = re.sub('KAREN ATTIAH:[\w.,!?\’\'\"\[\]: —\-…–;”“/]*\n\n', '', cleanedText)
    cleanedText = re.sub('JAMIE RILEY:[\w.,!?\’\'\"\[\]: —\-…–;”“/]*\n\n', '', cleanedText)
    cleanedText = re.sub('MICHAEL LARABEE:[\w.,!?\’\'\"\[\]: —\-…–;”“/]*\n\n', '', cleanedText)
    cleanedText = re.sub('JAMES DOWNIE:[\w.,!?\’\'\"\[\]: —\-…–;”“/]*\n\n', '', cleanedText)
    cleanedText = re.sub('DIEHL:[\w.,!?\’\'\"\[\]: —\-…–;”“/]*\n\n', '', cleanedText)
    cleanedText = re.sub('RYAN:[\w.,!?\’\'\"\[\]: —\-…–;”“/]*\n\n', '', cleanedText)
    cleanedText = re.sub('LANE:[\w.,!?\’\'\"\[\]: —\-…–;”“/]*\n\n', '', cleanedText)
    cleanedText = re.sub('TOM TOLES, EDITORIAL CARTOONIST:[\w.,!?\’\'\"\[\]: —\-…–;”“/]*\n\n', '', cleanedText)
    cleanedText = re.sub('LEWANDOWSKI:[\w.,!?\’\'\"\[\]: —\-…–;”“/]*\n\n', '', cleanedText)
    cleanedText = re.sub('RUTH MARCUS:[\w.,!?\’\'\"\[\]: —\-…–;”“/]*\n\n', '', cleanedText)
    cleanedText = re.sub('CHARLES LANE, EDITORIAL WRITER/COLUMNIST:[\w.,!?\’\'\"\[\]: —\-…–;”“/]*\n\n', '', cleanedText)
    cleanedText = re.sub('RUTH MARCUS, COLUMNIST:[\w.,!?\’\'\"\[\]: —\-…–;”“/]*\n\n', '', cleanedText)
    cleanedText = re.sub('MARCUS:[\w.,!?\’\'\"\[\]: —\-…–;”“/]*\n\n', '', cleanedText)
    cleanedText = re.sub('STEPHEN STROMBERG, EDITORIAL WRITER:[\w.,!?\’\'\"\[\]: —\-…–;”“/]*\n\n', '', cleanedText)
    cleanedText = re.sub('JO-ANN ARMAO, ASSOCIATE EDITORIAL PAGE EDITOR:[\w.,!?\’\'\"\[\]: —\-…–;”“/]*\n\n', '', cleanedText)
    cleanedText = re.sub('ATTIAH:[\w.,!?\’\'\"\[\]: —\-…–;”“/]*\n\n', '', cleanedText)
    cleanedText = re.sub('CORY:[\w.,!?\’\'\"\[\]: —\-…–;”“/]*\n\n', '', cleanedText)

    # Remove stage directions
    cleanedText = re.sub('\[CROSSTALK\]\n\n', '', cleanedText)
    cleanedText = re.sub('\[Crosstalk\]\n\n', '', cleanedText)
    cleanedText = re.sub('\[Silence\]\n\n', '', cleanedText)
    cleanedText = re.sub('\(Applause\)\n\n', '', cleanedText)
    cleanedText = re.sub('\[Break in video\]\n\n', '', cleanedText)

    # Create new file after parsing and cleaning
    with io.FileIO("cleanedText.txt", "w") as file:
        file.write(cleanedText)

if __name__ == '__main__':
    print("Running cleaning script")
    cleanTextFile()



    # (Applause)
    # Name of person speaking:
    # [A-z][.?!][A-z] to include a space
