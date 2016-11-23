"""
Different checkers and tries...
"""

import win32service
import importlib
# import work_with_doc.doc_searcher as doc_searcher

"""
name = 'work_with_doc.lpdmn'
components = name.split('.')
mod = __import__(components[0])
for com in components[1:]:
    mod = getattr(mod, com)
    print(mod.__name__)
"""

# mod = __import__('work_with_doc.doc_searcher', fromlist=['ldpmn'])
#
# funk = getattr(mod, 'ldpmn')
# # help(doc_searcher)
# print(mod.__name__)

# print(mod.__doc__)

# mod(win32service)

help(win32service)

print(win32service.__dict__)
# help(sys.getwindowsversion())
#
# print(sys.getwindowsversion().__doc__)
# s = sys.getwindowsversion().__doc__