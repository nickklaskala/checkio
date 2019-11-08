#!/usr/bin/env checkio --domain=py run morse-clock

def checkio(ts: str) -> str:
	h,m,s=[t.zfill(2) for t in ts.split(':')]
	bin = lambda t,zeros: str(format(int(t), 'b').zfill(zeros))

	mc=bin(h[0],2)+' '+bin(h[1],4)+' : '+bin(m[0],3)+' '+bin(m[1],4)+' : '+bin(s[0],3)+' '+bin(s[1],4)
	return (mc.replace('0','.').replace('1','-'))



if __name__ == '__main__':
	print("Example:")
	assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
	assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
	assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
	assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
	print("Coding complete? Click 'Check' to earn cool rewards!")
