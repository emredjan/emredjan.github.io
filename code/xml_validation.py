from lxml import etree
from io import StringIO #from StringIO... for python2
import sys

# Declare filenames to be used
# Check if input arguments are ok
try:
    filename_xml = sys.argv[1]
    filename_xsd = sys.argv[2]
except:
    print('Please enter xml & schema filenames as program arguments.\n'
          'Usage: "python validation.py <filename_xml(.xml)> <filename_xsd(.xsd)>"')
    quit()
    
filename_error_syntax = 'error_syntax.log'
filename_error_valid = 'error_schema.log'


# open and read schema file
with open(filename_xsd, 'r') as schema_file:
    schema_to_check = schema_file.read()

# open and read xml file
with open(filename_xml, 'r') as xml_file:
    xml_to_check = xml_file.read()

# load schema
xmlschema_doc = etree.parse(StringIO(schema_to_check))
xmlschema = etree.XMLSchema(xmlschema_doc) 

# parse xml
try:
    doc = etree.parse(StringIO(xml_to_check))
    print('\nXML well formed, syntax ok.')
    
except IOError:
    print('\nInvalid File')
    
except etree.XMLSyntaxError as err:
    print('\nXMLSyntaxError: See ' + filename_error_syntax + '\n')
    with open(filename_error_syntax, 'w') as error_log_file:
        error_log_file.write(str(err.error_log))
    quit()
    
except:
    print('\nUnknown error, exiting.\n')
    quit()
    
# validate against schema
# print(xmlschema.validate(doc))
try:
    xmlschema.assertValid(doc)
    print('\nXML valid, schema validation ok.\n')
    
except etree.DocumentInvalid as err:
    print('\nSchema validation error: See ' + filename_error_valid + '\n')
    with open(filename_error_valid, 'w') as error_log_file:
        error_log_file.write(str(err.error_log))
    quit()
    
except:
    print('\nUnknown error, exiting.\n')
    quit()
