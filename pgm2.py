import re,threading

class MRObject:
	def __init__(self,key,value):
		self.key=key
		self.value=value

result=[]

def _computeKeys(line):
	mrobjects=[]
	words=re.findall(r'\w+',line.strip())
	for word in words:
		mrobjects.append(MRObject(word,1))
	result.extend(mrobjects)

def _mapper(contents):
	threads=[]
	for line in contents:
		process = threading.Thread(target=_computeKeys, args=(line,))
		process.start()
		threads.append(process)
	for process in threads:
		process.join()

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
	_mapper(contents)
	mrdict=_reducer(result)
	fd.close()
	print "Frequency of each word:"
	for word in mrdict.keys():
		print word," --> ",mrdict[word]


mapReduce('file1.txt')