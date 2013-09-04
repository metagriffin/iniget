# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# file: $Id$
# auth: metagriffin <metagriffin@uberdev.org>
# date: 2013/09/04
# copy: (C) CopyLoose 2013 UberDev <hardcore@uberdev.org>, No Rights Reserved.
#------------------------------------------------------------------------------

import six, json, iniherit, collections
from six.moves import configparser

DEFAULT_SECTION = configparser.DEFAULTSECT

#------------------------------------------------------------------------------
def isstr(obj):
  return isinstance(obj, six.string_types)

#------------------------------------------------------------------------------
class Config(collections.OrderedDict): pass
class Section(collections.OrderedDict): pass

#------------------------------------------------------------------------------
def sectcmp(a, b):
  if a == b:
    return 0
  if a == DEFAULT_SECTION:
    return -1
  if b == DEFAULT_SECTION:
    return 1
  return cmp(a, b)

truthy = frozenset(('true', 'yes', 'on'))
falsy  = frozenset(('false', 'no', 'off'))

#------------------------------------------------------------------------------
class Loader(object):

  #----------------------------------------------------------------------------
  def __init__(self, inherit=True, case_sensitive=True,
               defaults=None, interpolate=True,
               jsonify=True):
    self.inherit      = inherit
    self.case         = case_sensitive
    self.defaults     = defaults
    self.interpolate  = interpolate
    self.jsonify      = jsonify

  #----------------------------------------------------------------------------
  def loadfp(self, fp):
    attr = 'SafeConfigParser' if self.interpolate else 'RawConfigParser'
    mod  = iniherit if self.inherit else configparser
    ini  = getattr(mod, attr)(defaults=self.defaults)
    ini.optionxform = str if self.case else str.lower
    ini.readfp(fp)
    ret = Config(((DEFAULT_SECTION, ini.defaults()),))
    for section in sorted(ini.sections(), cmp=sectcmp):
      ret[section] = Section(ini.items(section))
    if self.jsonify is False:
      return ret
    jret = Config()
    for sectname, options in ret.items():
      section = Section()
      for option, value in options.items():
        section[option] = self.parse(value)
      jret[sectname] = section
    return jret

  #----------------------------------------------------------------------------
  def parse(self, value):
    if value in truthy:
      return True
    if value in falsy:
      return False
    try:
      # todo: make this sensitive to self.jsonify being a range of values...
      #       eg. at jsonify==0.1, only parse scalars. at jsonify=0.2, also
      #       parse lists. at jsonify>=1.0 and is True, go all out.
      return json.loads(value)
    except ValueError:
      return value

default = Loader()

#------------------------------------------------------------------------------
def load(fp, loader=None, *args, **kw):
  if loader is None:
    if args or kw:
      loader = Loader(*args, **kw)
    else:
      loader = default
  if isstr(fp):
    with open(fp, 'rb') as fp:
      return load(fp, loader=loader)
  return loader.loadfp(fp)

#------------------------------------------------------------------------------
def loads(data, *args, **kw):
  return load(six.StringIO(data), *args, **kw)

#------------------------------------------------------------------------------
# end of $Id$
#------------------------------------------------------------------------------
