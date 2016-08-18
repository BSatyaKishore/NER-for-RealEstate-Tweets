import re
digitMatch = r"[0-9][-.]?[0-9][-.]?[0-9][-.]?[0-9][-.]?[0-9][-.]?[0-9][-.]?[0-9][-.]?[0-9][-.]?[0-9][-.]?"
namesFile = open('names.txt','r')
surnamesFile = open('surname.txt','r')
Locations = open('locality','r')
DelhiNCRLocations = open('DelhiNcrLocations.txt','r')
AttributeList = open('attr','r')
name_list = namesFile.readlines()
surname_list = surnamesFile.readlines()
localities = Locations.readlines()
delhiLocations = DelhiNCRLocations.readlines()
attributes = AttributeList.readlines()
locations = []
attributeList = ['ac','tv']

for i in range(len(name_list)):
	name_list[i] = name_list[i].lower().strip()
for i in range(len(surname_list)):
	surname_list[i] = surname_list[i].lower().strip()

def NumType(s):	
	count = 0
	for i in s:
		if i in ' 0123456789,#@/-+':
			count += 1
		else:
			return "NOT_NUM"
	if count > 7:
		return "BIG_NUM"
	else:
		return "SMALL_NUM"

for i in range(len(localities)):
	sa = localities[i].strip().lower()
	if sa == '':
		continue
	if '#' == sa[0]:
		sa = sa[1:]
	if len(sa) > 2:
		if NumType(sa) == 'NOT_NUM':
			locations.append(sa)

for i in range(len(attributes)):
	sa = attributes[i].strip().lower()
	if len(sa) > 2:
		attributeList.append(sa)

# Link 
def is_link(s):
	if ("http://" or "https://" or "www." or ".com" or ".html") in s.lower():
		return True
	return False

def has_9Digits(s):
	if re.search(digitMatch,s):
		return True
	return False

digitMatcher = r"[0-9][-.,]?([0-9][-.,]?)*"
def hasNum(s):
	if re.search(digitMatcher,s):
		return True
	return False

def isInNamesList(name):
	s = name.lower().strip()
	if len(s) < 1:
		return 'NOT_NAME'
	for j in surname_list:
		if j in s:
			return 'SURNAME'
	for j in name_list:
		if j in s:
			return 'NAME'
	return 'NOT_NAME'

def isContact(s):
	if ("call" or "contact") in s.lower():
		return True
	return False

def isIn(s):
	if 'in' in s.lower():
		return True
	return False

def isAt(s):
	if 'at' in s.lower():
		return True
	return False

def startsWithHash(s):
	if '#' == s[0]:
		return True
	return False

def startsWithAt(s):
	if '@' == s[0]:
		return True
	return False

def hasLocation(s):
	for i in locations:
		if i in s.lower():
			return True
	return False

def isBuildingAttributes(s):
	if 'floor' in s.lower():
		return 'FLOOR'
	if 'bhk' in s.lower():
		return 'BHK'

def isPer(s):
	if ('per' or 'psf' or '/sq' or '/sq' or '/f' or '/-sq' or 'psq' or '/metr' or '/mtr' or '/ft' or '/sft' or 'psft' or 'par' or 'syrd' or 'ka' or 'bsp') in s.lower():
		return True
	return False

def isAreaUnit(s):
	if ('acre' or 'square' or 'miters' or 'sqrd' or 'sqft' or 'sqm' or 'area' or 'size' or 'sq.ft' or 'sq.mt' or 'mtr' or 'metr' or 's/f' or 'meter' or 'mater' or 'gaj' or 'metar' or 'miter' or 'space' or 'sft' or 'sqyd' or 'yards' or 'yd' or 'yrd' or 'spft' or 'feet' or 'size') in s.lower():
		return True
	return False


# Some number followed by digits and cr or l or k
def isPrice(s):
	a = False
	sa = s.lower().strip()
	for i in range(len(sa)):
		if sa[i] in ['0','1','2','3','4','5','6','7','8','9',',','.',' ']:
			a = True
		else:
			if a:
				if ((sa[i:i+2] == 'cr') or (sa[i] == 'l') or (sa[i] == 'k')):
					return True
				else:
					return False
	return False

quantifiers = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th','15th','16th','17th','18th','19th','20th']
def hasQuantifier(s):
	for i in quantifiers:
		if i in s.lower():
			return True
	return False

def isInAttributeList(s):
	for i in attributeList:
		if i in s.lower():
			return True
	return False

def numInParts(s1,s2,s3):
	return NumType(s1+s2+s3)

#print isInAttributeList('satya')