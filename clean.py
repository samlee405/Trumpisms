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
    cleanedText = re.sub('(Unknown|ATTIAH|CORY|LEWANDOWSKI|MARCUS|JO-ANN ARMAO, ASSOCIATE EDITORIAL PAGE EDITOR|STEPHEN STROMBERG, EDITORIAL WRITER|RUTH MARCUS|RUTH MARCUS, COLUMNIST|RYAN|CHARLES LANE, EDITORIAL WRITER/COLUMNIST|LANE|DIEHL|TOM TOLES, EDITORIAL CARTOONIST|JAMES DOWNIE|MICHAEL LARABEE|CHRISTINE EMBA|KAREN ATTIAH|JAMIE RILEY|ARMAO|Billy Bush|HOPE HICKS, TRUMP CAMPAIGN SPOKESPERSON|Bush|Arianne Zucker|Zucker|FRED HIATT|STROMBERG|HIATT):[\w.,!?\’\'\"\[\]: —\-…–;”“/]*\n\n', '', rawText)

    # Remove Trump: prefixes from transcripts
    cleanedText = re.sub('(Trump|Donald J. Trump|President-elect):', '', cleanedText)

    # Remove stage directions
    cleanedText = re.sub(' ?(\[CROSSTALK\]|\[Crosstalk\]|\[crosstalk\])', '', cleanedText)
    cleanedText = re.sub(' ?\[Silence\]', '', cleanedText)
    cleanedText = re.sub(' ?(\(Applause\)|\[applause\])', '', cleanedText)
    cleanedText = re.sub(' ?\[Break in video\]', '', cleanedText)
    cleanedText = re.sub(' ?\(Laughter\)|\[laughter\]', '', cleanedText)
    cleanedText = re.sub(' ?\(inaudible\)', '', cleanedText)
    cleanedText = re.sub(' ?\(OFF-MIKE\)', '', cleanedText)

    # cleanedText = re.sub(r'([a-z]\.)([A-Z])', r'\1 \2', cleanedText) eergerigegberjnkeghj

    # Remove other miscellaneous text
    cleanedText = re.sub('SPEECH \d', '', cleanedText)

    # Fix sentence spacing (add a space after every period and then remove any instance of two consecutive white spaces)
    cleanedText = cleanedText.replace('.', '. ')
    cleanedText = cleanedText.replace('?', '? ')
    cleanedText = cleanedText.replace('  ', ' ')

    # Create new file after parsing and cleaning
    with io.FileIO("cleanedText.txt", "w") as file:
        file.write(cleanedText)

if __name__ == '__main__':
    print("Running cleaning script")
    cleanTextFile()



    # (Applause)
    # Name of person speaking:
    # [A-z][.?!][A-z] to include a space
