# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# file: $Id$
# auth: metagriffin <metagriffin@uberdev.org>
# date: 2013/09/04
# copy: (C) CopyLoose 2013 UberDev <hardcore@uberdev.org>, No Rights Reserved.
#------------------------------------------------------------------------------

import six
from .loader import DEFAULT_SECTION, configparser, Config, Section, isstr, sectcmp

#------------------------------------------------------------------------------
def sift(data,
         list_sections=False, list_keys=False,
         sections=None, keys=None):

  if list_sections:
    return sorted(data.keys(), cmp=sectcmp)

  if list_keys:
    if isstr(sections):
      try:
        return sorted(data[sections].keys())
      except KeyError:
        raise configparser.NoSectionError(section=sections)
    try:
      ret = Config()
      for section in sorted(sections or data.keys(), cmp=sectcmp):
        ret[section] = sorted(data[section].keys())
      return ret
    except KeyError as err:
      raise configparser.NoSectionError(section=err.message)

  if isstr(sections):
    if sections not in data:
      raise configparser.NoSectionError(section=sections)
    section = data[sections]
    if isstr(keys):
      try:
        return section[keys]
      except KeyError:
        raise configparser.NoOptionError(section=sections, option=keys)
    if keys is None:
      return section
    try:
      ret = Section()
      for key in sorted(keys):
        ret[key] = section[key]
      return ret
    except KeyError:
      raise configparser.NoOptionError(section=sections, option=keys)

  ret = Config()
  for sectname in sorted(sections or data.keys(), cmp=sectcmp):
    if sectname not in data:
      raise configparser.NoSectionError(section=sectname)
    section = data[sectname]
    ret[sectname] = Section()
    for key in sorted(keys or section.keys()):
      if key not in section:
        raise configparser.NoOptionError(section=sectname, option=key)
      ret[sectname][key] = section[key]
  return ret


#------------------------------------------------------------------------------
# end of $Id$
#------------------------------------------------------------------------------
