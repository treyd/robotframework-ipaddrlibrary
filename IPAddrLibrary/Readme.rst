=============
IPAddrLibrary
=============
-------------------------------------------------------------------------------------------
A Robot Framework library for querying address and hostnames, and performing IP subnet math
-------------------------------------------------------------------------------------------

IPAddrLibrary is a library for Robot Framework which provides keywords for
manipulating IP addresses and hostnames.  This library will provide basic
host-to-ip and ip-to-host conversion, as well as IP address subnet math.

This library depends on python-iplib (http://www.mimante.net/soft/iplib)

Installation
============

   1. Download latest tar.gz from dist directory
   1. Unzip to your Robot Framework library directory
   1. Add "IPAddrLibrary" to your test suite's Settings table, e.g::
   
   *** Settings ***
   | Library | ./IPAddrLibrary/ |
   
