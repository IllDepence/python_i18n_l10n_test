# -*- coding: utf-8 -*-

import gettext

t = gettext.translation('test', localedir='translations', fallback='true')
_ = t.gettext

print(_("This is a test."))
