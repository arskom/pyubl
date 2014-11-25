PyUBL
=====

This is a bunch of scripts that map UBL documents to python objects and vice
versa.

You need lxml and spyne>=2.12 (not released, so clone master from project repo)

Run examples/parse_schema.py to see an XMLDSIG document deserialized to a
Python object. The signature verification will probably fail because the document
is not canonical.

