#!/usr/bin/env checkio --domain=py run digits-doublets

# .story .shadow {        float: left;        /*padding: 10px;*/        margin: 10px;        border: black;        /*box-shadow: 0 0 20px 10px rgba(0, 0, 0, 1);*/        /*-moz-box-shadow: 0 0 20px 10px rgba(0, 0, 0, 1);*/        /*-webkit-box-shadow: 0 0 20px 10px rgba(0, 0, 0, 1);*/    }    .story .left {        float: left;    }    .story .right {        float: right;    }    .story .title {        font-weight: bold;        margin: 20px 0 20px 0;    }
# END_DESC

def checkio(numbers):
	return []

numbers=[123, 991, 323, 321, 329, 121, 921, 125, 999]
numbers=[str(i) for i in numbers]
start,end,midnums=numbers[0],numbers[-1],numbers[1:]
masterlist=[]
dct={}
for i in numbers:
	dct[i]=[n for n in numbers if ((1 if i[0] in n[0] else 0) + (1 if i[1] in n[1] else 0) + (1 if i[2] in n[2] else 0))==2]


def probe(i,hard_path):
	soft_path=hard_path
	if hard_path[-1]==end:
		return {'winner':'yes', 'path':hard_path}
	
	if end in dct[i]:
		masterlist.apped(hardpath+[end])
		return {'winner':'yes', 'path':path+[end]}
	if all([num in path for num in dct[i]]):
		return {'winner':'no' , 'path':[]}
	else:
		for num in dct[i]:
			if num in path:
				continue
			probe(num,hard_path+[num])
	return'dead'

path=[start]

for i in dct[path[-1]]:
	tmp=probe(i,path)
	if tmp['winner']=='yes':
		masterlist=tmp[path]






#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '_x_main__':
	assert checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]) == [123, 121, 921, 991, 999], "First"
	assert checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]) == [111, 121, 127, 727, 777], "Second"
	assert checkio([456, 455, 454, 356, 656, 654]) == [456, 454, 654], "Third, [456, 656, 654] is correct too"