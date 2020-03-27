#!/usr/bin/env checkio --domain=py run digits-doublets

# .story .shadow {        float: left;        /*padding: 10px;*/        margin: 10px;        border: black;        /*box-shadow: 0 0 20px 10px rgba(0, 0, 0, 1);*/        /*-moz-box-shadow: 0 0 20px 10px rgba(0, 0, 0, 1);*/        /*-webkit-box-shadow: 0 0 20px 10px rgba(0, 0, 0, 1);*/    }    .story .left {        float: left;    }    .story .right {        float: right;    }    .story .title {        font-weight: bold;        margin: 20px 0 20px 0;    }
# END_DESC

def checkio(numbers):
	numbers=[str(i) for i in numbers]
	start,end=numbers[0],numbers[-1]
	masterlist=[]
	nodedct={i:[n for n in numbers if ((1 if i[0] in n[0] else 0) + (1 if i[1] in n[1] else 0) + (1 if i[2] in n[2] else 0))==2] for i in numbers}


	def probe(i,hard_path):
		soft_path=hard_path+[i]
		if hard_path[-1]==end:
			return {'winner':'yes', 'path':soft_path}
		
		if end in nodedct[i]:
			masterlist.append(soft_path+[end])
			return {'winner':'yes', 'path':soft_path+[end]}
		if all([num in soft_path for num in nodedct[i]]):
			return {'winner':'no' , 'path':[]}
		else:
			for num in nodedct[i]:
				if num in soft_path:
					continue
				probe(num,soft_path)
		return'dead'

	for node in nodedct[start]:
		tmp=probe(node,[start])
	
	return list(map(int,min(masterlist,key=len)))



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]) == [123, 121, 921, 991, 999], "First"
	assert checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]) == [111, 121, 127, 727, 777], "Second"
	assert checkio([456, 455, 454, 356, 656, 654]) == [456, 454, 654], "Third, [456, 656, 654] is correct too"