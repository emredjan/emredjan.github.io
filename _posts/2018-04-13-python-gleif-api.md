---
layout:     post
title:      Python Wrapper for GLEIF Public API
date:       2018-04-13 11:20:00
summary:    A small wrapper I wrote in Python for GLEIF's public LEI lookup API
categories: blog
tags:       python api wrapper lei gleif
published:  true
---

This is a small thing that I started as a necessity for work: We needed to get [LEI](https://en.wikipedia.org/wiki/Legal_Entity_Identifier) (Legal Entity Identifier) registration information for our customers, and using GLEIF's (Global LEI Foundation) public API to query things with Python was convenient at that time. Thinking of reusability, I structured it as a module, covering most of our use cases. Code is now in github, maybe it helps others that need an easier way to query LEI numbers.

To access, go to [https://github.com/emredjan/leipy](https://github.com/emredjan/leipy) and download the repository (in fact you only need the file `leipy/gleif.py`). You will need `requests` and `dateutil` libraries, and optionally `pandas` if you want DataFrame output of results, which should all be included with a standard anaconda installation.

You can use it as:

```python
from leipy import GLEIF

gleif = GLEIF(api_version='v1')

raw_output, results, results_df = gleif.request(
	['HWUPKR0MPOU8FGXBT394','7ZW8QJWVPR4P1J1KQY45'],
	return_dataframe=True
)
```

GLEIF API has a limit of 200 LEIs per request, my wrapper handles that for you, you can provide more than 200 LEIs.
It returns the raw json output from the API, a results class and optionally a pandas DataFrame.

Raw json (as a list of dicts), which you can further process as you please, looks like this:
```python
[{'LEI': {'$': 'HWUPKR0MPOU8FGXBT394'},
  'Entity': {'LegalName': {'$': 'Apple Inc.'},
   'LegalAddress': {'Line1': {'$': 'C/O C T Corporation System'},
    'Line2': {'$': '818 West 7th Street'},
    'Line3': {'$': 'Suite 930'},
    'City': {'$': 'Los Angeles'},
    'Region': {'$': 'US-CA'},
    'Country': {'$': 'US'},
    'PostalCode': {'$': '90017'}},
   'HeadquartersAddress': {'Line1': {'$': '1 Infinite Loop'},
    'City': {'$': 'Cupertino'},
    'Region': {'$': 'US-CA'},
    'Country': {'$': 'US'},
    'PostalCode': {'$': '95014'}},
   'BusinessRegisterEntityID': {'@register': 'RA000598', '$': 'C0806592'},
   'LegalJurisdiction': {'$': 'US'},
   'LegalForm': {'$': 'INCORPORATED'},
   'EntityStatus': {'$': 'ACTIVE'}},
  'Registration': {'InitialRegistrationDate': {'$': '2012-06-06T15:53:00.000Z'},
   'LastUpdateDate': {'$': '2017-12-12T21:19:00.000Z'},
   'RegistrationStatus': {'$': 'ISSUED'},
   'NextRenewalDate': {'$': '2018-12-13T00:31:00.000Z'},
   'ManagingLOU': {'$': 'EVK05KS7XY1DEII3R011'},
   'ValidationSources': {'$': 'FULLY_CORROBORATED'}}},
 {'LEI': {'$': '7ZW8QJWVPR4P1J1KQY45'},
  'Entity': {'LegalName': {'$': 'Google LLC'},
   'LegalAddress': {'Line1': {'$': 'C/O Corporation Service Company'},
    'Line2': {'$': '251 Little Falls Drive'},
    'City': {'$': 'Wilmington'},
    'Region': {'$': 'US-DE'},
    'Country': {'$': 'US'},
    'PostalCode': {'$': '19808'}},
   'HeadquartersAddress': {'Line1': {'$': '1600 Amphitheatre Parkway'},
    'City': {'$': 'Mountain View'},
    'Region': {'$': 'US-CA'},
    'Country': {'$': 'US'},
    'PostalCode': {'$': '94043'}},
   'BusinessRegisterEntityID': {'@register': 'RA000602', '$': '3582691'},
   'LegalJurisdiction': {'$': 'US'},
   'LegalForm': {'$': 'LIMITED LIABILITY COMPANY'},
   'EntityStatus': {'$': 'ACTIVE'}},
  'Registration': {'InitialRegistrationDate': {'$': '2012-06-06T15:52:00.000Z'},
   'LastUpdateDate': {'$': '2018-03-28T17:00:00.000Z'},
   'RegistrationStatus': {'$': 'ISSUED'},
   'NextRenewalDate': {'$': '2018-08-17T18:10:00.000Z'},
   'ManagingLOU': {'$': 'EVK05KS7XY1DEII3R011'},
   'ValidationSources': {'$': 'FULLY_CORROBORATED'}}}]
```

The results class, with easily accesible members for most commonly used LEI information can be accessed as this:

```python
>>> print(results.legal_name)
['Apple Inc.', 'Google LLC']

>>> print(results.lei_reg_status)
['ISSUED', 'ISSUED']

>>> print(results.date_last_updated)
[datetime.datetime(2017, 12, 12, 21, 19, tzinfo=tzutc()),
 datetime.datetime(2018, 3, 28, 17, 0, tzinfo=tzutc())]
```

And if you opt for a DataFrame, the results will be conveniently flattened and ready for further processing for you:

```python
>>>results_df
```

| |country_hq|country_legal|date_initial_reg|date_last_updated|date_next_renewal|legal_name|lei|lei_reg_status|status|
|-|----------|-------------|----------------|-----------------|-----------------|----------|---|--------------|------|
|0	|US	|US	|2012-06-06 15:53:00+00:00	|2017-12-12 21:19:00+00:00	|2018-12-13 00:31:00+00:00	|Apple Inc.	|HWUPKR0MPOU8FGXBT394	|ISSUED	|ACTIVE|
|1	|US	|US	|2012-06-06 15:52:00+00:00	|2018-03-28 17:00:00+00:00	|2018-08-17 18:10:00+00:00	|Google LLC	|7ZW8QJWVPR4P1J1KQY45	|ISSUED	|ACTIVE|



As I said, this is more suited to our use case, and it's like a hobby project for me. If you need a more generic solution for python check out [pygleif](https://github.com/ggravlingen/pygleif), or you can always go for the [GLEIF REST API](https://www.gleif.org/en/lei-data/gleif-lei-look-up-api/access-the-api) itself.

Next steps for me is to add a solution for automatically downloading and parsing XML and CSV files from GLEIF, and putting everything in a package for easier use (pip and/or conda).

Until then, enjoy!
