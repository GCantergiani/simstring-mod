#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
A Unicode sample.

We assume that the source code is written in UTF-8 encoding (see the
encoding declaration in line 2). We can use 8-bit strings as they are
with SimString.
"""

import simstring

# Open a SimString database for writing with Unicode mode.
db = simstring.writer('sample_unicode.db', 3, False, True)

# Write a string, and close the database.
db.insert('スパゲティ', 12345678901234)
db.close()


# Open the SimString database for reading.
db = simstring.reader('sample_unicode.db')

# Set a similarity measure and threshold.
db.measure = simstring.cosine
db.threshold = 0.6

# Use an 8-bit string encoded in UTF-8.
print ' '.join([str(i) for i in db.retrieve('スパゲティー')])

# Convert a Unicode object into an UTF-8 query string.
print ' '.join([str(i) for i in db.retrieve(u'スパゲティー'.encode('utf-8'))])

