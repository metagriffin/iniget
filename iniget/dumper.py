# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# file: $Id$
# auth: metagriffin <metagriffin@uberdev.org>
# date: 2013/09/04
# copy: (C) CopyLoose 2013 UberDev <hardcore@uberdev.org>, No Rights Reserved.
#------------------------------------------------------------------------------

import six, json
from .loader import configparser, Config, Section, isstr, sectcmp

list_types = (list, tuple, set)

#------------------------------------------------------------------------------
class Dumper(object):

  #----------------------------------------------------------------------------
  def __init__(self, jsonify=False):
    self.jsonify = jsonify

  #----------------------------------------------------------------------------
  def dumpfp(self, data, fp, jsonify_lists=False):
    if self.jsonify:
      fp.write(json.dumps(data))
      fp.write('\n')
      return
    if isinstance(data, Config):
      for section, options in data.items():
        # todo: ensure this escape mechanism is ok with ConfigParser...
        section = section.replace('\\', '\\\\').replace(']', '\\]')
        fp.write('[{}]\n'.format(section))
        self.dumpfp(options, fp)
      return
    if isinstance(data, Section):
      for option, value in data.items():
        fp.write(option)
        fp.write(' = ')
        self.dumpfp(data[option], fp, jsonify_lists=True)
      return
    if not jsonify_lists and isinstance(data, list_types):
      for item in data:
        fp.write(item)
        fp.write('\n')
      return
    if isstr(data):
      fp.write(data)
    else:
      fp.write(json.dumps(data))
    fp.write('\n')

default = Dumper()

#------------------------------------------------------------------------------
def dump(data, fp, dumper=None, *args, **kw):
  if dumper is None:
    if args or kw:
      dumper = Dumper(*args, **kw)
    else:
      dumper = default
  if isstr(fp):
    with open(fp, 'rb') as fp:
      return dump(data, fp, dumper=dumper)
  return dumper.dumpfp(data, fp)

#------------------------------------------------------------------------------
def dumps(data, *args, **kw):
  out = six.StringIO()
  dump(data, out, *args, **kw)
  return out.getvalue()

#------------------------------------------------------------------------------
# end of $Id$
#------------------------------------------------------------------------------
