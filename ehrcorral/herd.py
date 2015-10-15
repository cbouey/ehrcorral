# -*- coding: utf-8 -*-
"""Contains core classes and functions for defining populations and acting upon
them.
"""
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

from collections import namedtuple


RECORD_FIELDS = (
    'first_name',
    'middle_name',
    'last_name',
    'suffix',
    'address',
    'sex',
    'gender',
    'ssn',
    'birthdate',
    'blood_type',
)

META_FIELDS = (
    'id',
    'soundex',
    'nysiis',
    'metaphone',
    'dmetaphone',
)


class Record(namedtuple('Record', RECORD_FIELDS)):
    __slots__ = ()  # Prevent per-instance dictionaries to reduce memory


class Herd(object):
    """A collection of :py:class:`._Record`s with methods for interacting with
    and linking records in the herd.

    You need:
    - validate names (check for commas, weird chars, convert to unicode/ascii?)
        * remove Mrs, PhD, Ms., etc.
        * check for commas, weird chars
        * convert to unicode/ascii?
    - validate that you only have certain field names in the incoming dict
    - parse names into first, last, prefix, suffix

    need to make separate .csv's for each region
    get male and female names and combine
    only use the No. 1, No. 2, and No. 3 names
    download whatever is in the first <a> (some names will be left out)
    split by / and add to list
    split by , and add to list
    split by ( and remove whatever comes after the opening parenthesis
              then convert everything to ASCII (i.e. need to remove accented
                                                characters, umlaus)

              when you generate a single file, you might make 1000 names and
              make the population of names representative of the population of
              ethnicities in the US. or just compare separately.

              what do you do with names with JR...SR...I...II?

    HAVE ABILITY to grow a herd, which doesn't mean adding to the tuple of
    Records...have it be a way around memory limitations. That means that
    instead of 'appending' to the tuple of Records, it immediately sends
    the data to append to the ES database. It should therefore be that you
    require a connection object in order to create a herd (maybe not).

    """
    def __init__(self):
        self.population = ()

    def __str__(self):
        population = self.population
        if len(population) > 6:
            return "[\n  {},\n  {},\n  {}\n...,\n  {},\n  {}\n]".format(
                population[0],
                population[1],
                population[2],
                population[-2],
                population[-1]
            )
        else:
            return str(population)

#    def __repr__(self):
#        return "Herd(population={})".format(str(self))

    def populate(self, records):
        """Sets the Herd's sub-population.

        Args:
            records (list, tuple): A list or tuple of :py:class:`._Record`s
        """
        if not isinstance(records, (tuple, list)):
            raise ValueError("Expected a tuple or list.")
        if isinstance(records, list):
            records = tuple(records)
        self.population = records
