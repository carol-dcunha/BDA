import re

class MRObject:
	def __init__(self,key,value):
		self.key=key
		self.value=value


def _mapper(contents):
	mrobjects=[]
	for line in contents:
		words=re.findall(r'\w+',line.strip())
		for word in words:
			mrobjects.append(MRObject(word,1))
	return mrobjects

def _reducer(mrobjects):
	mrdict={}
	for obj in mrobjects:
		if obj.key in mrdict.keys():
			mrdict[obj.key]+=obj.value
		else:
			mrdict[obj.key]=obj.value
	return mrdict

def mapReduce(tfile):
	fd=open(tfile)
	contents=fd.readlines()
	mrdict=_reducer(_mapper(contents))
	fd.close()
	print "Frequency of each word:"
	for word in mrdict.keys():
		print word," --> ",mrdict[word]


mapReduce('file1.txt')