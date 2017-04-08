from lxml import etree
from io import StringIO #from StringIO... for python2
import sys


# Declare filenames to be used
# Check if input arguments are ok
try:
    filename_xml_input = sys.argv[1]

except:
    print('Please enter xml filename as program argument.\n'
          'Usage: "python xml_trim.py <filename_xml_input(.xml)> "')
    quit()
    
input_split = filename_xml_input.rsplit('.', 1)
filename_xml_output = input_split[0] + '_trimmed.' + input_split[1]

filename_error_syntax = 'error_syntax_trimmed.log'

'''
print('\nOpening File\n')
with open(filename_xml_input, 'r') as f:
    content = f.readlines()

print('\nStripping Content\n')
content = [x.strip() for x in content]

print('\nStripping Content 2\n')
content_stripped = ''
for item in content:
    content_stripped += item+'\n'
'''

print('\nParsing XML')
# parse xml
parser = etree.XMLParser(remove_blank_text=True)

try:    
    #doc = etree.parse(StringIO(content), parser)
    doc = etree.parse(filename_xml_input, parser)
    print('\nXML well formed, syntax ok.')
    
except IOError:
    print('\nInvalid File\n')
    
except etree.XMLSyntaxError as err:
    print('\nXMLSyntaxError: See ' + filename_error_syntax + '\n')
    with open(filename_error_syntax, 'w') as error_log_file:
        error_log_file.write(str(err.error_log))
    quit()
    
# write trimmed pretty xml
with open(filename_xml_output, 'wb') as f: #'w' for python 2?
    f.write(etree.tostring(doc.getroot(), pretty_print=True, encoding='UTF-8'))

print('\nTrimmed file written as: ' + filename_xml_output + '\n')
