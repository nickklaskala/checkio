#!/usr/bin/env checkio --domain=py run seven-segment


def seven_segment(lit_seg, broken_seg):
	up_lit_seg=[c for c in lit_seg if c.isupper()]
	lw_lit_seg=[c for c in lit_seg if c.islower()]
	up_brk_seg=[c for c in broken_seg if c.isupper()]
	lw_brk_seg=[c for c in broken_seg if c.islower()]
	up_tot_seg=up_lit_seg+up_brk_seg
	lw_tot_seg=lw_lit_seg+lw_brk_seg
	upNumMap={00:['A','B','C','D','E','F'], 10:['B','C'], 20:['A','B','G','E','D'], 30:['A','B','G','C','D'], 40:['F','G','B','C'], 50:['A','F','G','C','D'], 60:['A','F','G','C','D','E'], 70:['A','B','C'], 80:['A','B','C','D','E','F','G'], 90:['A','B','C','D','F','G'], }
	lwNumMap={0 :['a','b','c','d','e','f'], 1 :['b','c'], 2 :['a','b','g','e','d'], 3 :['a','b','g','c','d'], 4 :['f','g','b','c'], 5 :['a','f','g','c','d'], 6 :['a','f','g','c','d','e'], 7 :['a','b','c'], 8 :['a','b','c','d','e','f','g'], 9 :['a','b','c','d','f','g'], }

	up=[num for num,nset in upNumMap.items() if set(up_lit_seg).issubset(nset) and set(nset).issubset(up_tot_seg)]
	lw=[num for num,nset in lwNumMap.items() if set(lw_lit_seg).issubset(nset) and set(nset).issubset(lw_tot_seg)]

	m=[u+l for u in up for l in lw]

	print(m)
	return len(m)





if __name__ == '__main__':
    assert seven_segment({'B', 'C', 'b', 'c'}, {'A'}) == 2, '11, 71'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'e'}) == 6, '15, 16, 35, 36, 75, 76'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'F', 'b', 'e'}) == 20, '15...98'
    print('"Run" is good. How is "Check"?')
