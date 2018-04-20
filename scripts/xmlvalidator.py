import lxml.etree as etree
import sys

args = sys.argv
file = sys.argv[1]   
print(file)

#file ='raw_data/fullcalib.xml'


def validateXMLFormatAndMissingValue(file):
    try:
        e = etree.parse(file)
    except Exception as ex:
        print(ex)
        sys.exit(0)
    for elt in e.iter():
        if elt.text in (None, ""):
            print ("The missing value is in:\n %s: '%s' " % (elt.tag, elt.text))
            print("The xpath of the tag with missing value:\n "+e.getpath(elt)+"\n")
            
validateXMLFormatAndMissingValue(file)

sys.stdout.flush()