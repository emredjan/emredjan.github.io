---
layout:     post
title:      Validating XML using lxml in Python
date:       2017-04-08 16:20:00
summary:    Validating XML documents with XSD schemas using lxml package in Python
categories: blog
tags:       xml lxml python
published:  true
---

Often when working with XML documents, it's required that we validate our document with a predefined schema. These schemas usually come in XSD ([XML Schema Definition](https://www.wikiwand.com/en/XML_Schema_(W3C))) files and while there are commercial and open source applications that can do these validations, it's more flexible and a good learning experience to do it using Python.

### Prerequisites

You need Python installed obviously (I'll be using Python 3, but the codes should work in Python 2 with minimal modifications). You'll also need the [**lxml**](http://lxml.de/3.0/index.html) package to handle schema validations. You can install it using pip:

{% highlight shell %}

$ pip install lxml

{% endhighlight %}

Or if you're a conda user:

{% highlight shell %}

$ conda install lxml

{% endhighlight %}

### Importing and using lxml

For XML schema validation, we need the `etree` module from the `lxml` package. Let's also import `StringIO` from the `io` package for passing strings as files to `etree`, as well as `sys` for handling input.

{% highlight python %}

from lxml import etree
from io import StringIO
import sys

{% endhighlight %}

I prefer giving file names as command line arguments to the python file as it simplifies the handling:

{% highlight python %}

filename_xml = sys.argv[1]
filename_xsd = sys.argv[2]

{% endhighlight %}

Let's open and read both files:

{% highlight python %}

# open and read schema file
with open(filename_xsd, 'r') as schema_file:
    schema_to_check = schema_file.read()

# open and read xml file
with open(filename_xml, 'r') as xml_file:
    xml_to_check = xml_file.read()

{% endhighlight %}

### Parsing XML and XSD files

We can parse the XML files/schemas using the `etree.parse()` method, and we can load the schema to memory using `etree.XMLSchema()`. As schemas usually arrive well-formed and correctly formatted, I skipped error checking here for the schema parsing.

{% highlight python %}

xmlschema_doc = etree.parse(StringIO(schema_to_check))
xmlschema = etree.XMLSchema(xmlschema_doc)

{% endhighlight %}

Next is the parsing of the actual XML document. I usually do error checking here to catch syntax errors and not well-formed XML documents. `lxml` throws and `etree.XMLSyntaxError` exception if it finds errors in the XML document and provides an `error_log` in the exception. We can write this to a file check the incorrect lines and tags:

{% highlight python %}

# parse xml
try:
    doc = etree.parse(StringIO(xml_to_check))
    print('XML well formed, syntax ok.')

# check for file IO error    
except IOError:
    print('Invalid File')

# check for XML syntax errors
except etree.XMLSyntaxError as err:
    print('XML Syntax Error, see error_syntax.log')
    with open('error_syntax.log', 'w') as error_log_file:
        error_log_file.write(str(err.error_log))
    quit()
    
except:
    print('Unknown error, exiting.')
    quit()

{% endhighlight %}

### Validating with Schema

At the final step we can validate our XML document against the XSD schema using `assertValid` method from `etree.XMLSchema`. This method will get our parsed XML file (in variable `doc` above) and try to validate is using the schema definitions. It throws an `etree.DocumentInvalid` exception with an `error_log` object as above. We can also write this to a file to check any invalid tags or values.

{% highlight python %}

# validate against schema
try:
    xmlschema.assertValid(doc)
    print('XML valid, schema validation ok.')
    
except etree.DocumentInvalid as err:
    print('Schema validation error, see error_schema.log')
    with open('error_schema.log', 'w') as error_log_file:
        error_log_file.write(str(err.error_log))
    quit()
    
except:
    print('Unknown error, exiting.')
    quit()

{% endhighlight %}

You can save this script (i.e. as 'validation.py')and use it with:

{% highlight shell %}

$ python validation.py <path_to_xml_file> <path_to_xsd_file>

{% endhighlight %}

Any errors will be written to 'error_syntax.log' and 'error_schema.log' files (in the same directory as your .py file) with timestamps, line number and detailed explanation of validation errors. You can check and correct your XML documents before validating using this script again.

`lxml` is quite an extensive and flexible package to handle and process XML and related files. Check the sources below for tutorials, references and more information.

### Sources

- [lxml documentation on XML parsing](http://lxml.de/parsing.html)
- [lxml documentation on XML validation](http://lxml.de/validation.html)
- John Shipman's [Python XML tutorial](http://infohost.nmt.edu/tcc/help/pubs/pylxml/web/index.html)