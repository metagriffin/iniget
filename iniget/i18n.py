# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# file: $Id$
# auth: metagriffin <metagriffin@uberdev.org>
# date: 2013/09/03
# copy: (C) CopyLoose 2013 UberDev <hardcore@uberdev.org>, No Rights Reserved.
#------------------------------------------------------------------------------

from gettext import gettext

#------------------------------------------------------------------------------
def _(message, *args, **kw):
  if args or kw:
    return gettext(message).format(*args, **kw)
  return gettext(message)

#------------------------------------------------------------------------------
# end of $Id$
#------------------------------------------------------------------------------
