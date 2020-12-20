#step 1: !pip uninstall googletrans
#step2 : !pip install googletrans==3.1.0a0
# " AttributeError: 'NoneType' object has no attribute 'group' "

import googletrans
from googletrans import Translator
t=Translator()
# print(googletrans.LANGUAGES)
a=t.translate("em dep lam nhe",src="vi",dest="en")
print(a.text)