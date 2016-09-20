# -*- coding: utf-8 -*-

import gettext
import sys

t = gettext.translation('test', localedir='translations', fallback='true')
_ = t.gettext

print(_("This is a test."))

num = int(sys.argv[1])
print(t.ngettext('You have {numUnreadMsgs} unread Message.', 'You have {numUnreadMsgs} unread Messages.', num).format(numUnreadMsgs=num))
