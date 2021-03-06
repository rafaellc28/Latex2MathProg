import difflib
from latex2mathprog.Compiler import *

compiler = None

def setup_module(module):
	module.compiler = Compiler()


def check_test(name1, name2):
	f1 = open(name1, 'r')
	f2 = open(name2, 'r')

	expected = f2.read()
	expected = expected[:-1] # remove last \n

	doc = f1.read()
	#compiler = Compiler()
	actual = compiler.compile(doc)

	expected=expected.splitlines(True)
	actual=actual.splitlines(True)

	diff = difflib.unified_diff(expected, actual)
	diff = list(diff)

	f1.close()
	f2.close()

	if len(diff) != 0:
		print(''.join(diff))

	assert len(diff) == 0

def check_test_num(num, with_declarations = False):
	if with_declarations:
		name1 = 'latex2mathprog/test/samples/lp'+str(num)+'_with_declarations.tex.equation'
		name2 = 'latex2mathprog/test/samples/output/lp'+str(num)+'_with_declarations.tex.mod'
	else:
		name1 = 'latex2mathprog/test/samples/lp'+str(num)+'.tex.equation'
		name2 = 'latex2mathprog/test/samples/output/lp'+str(num)+'.tex.mod'

	check_test(name1, name2)

def check_test_extras_num(num):
	name1 = 'latex2mathprog/test/samples/extras/test'+str(num)+'.tex.equation'
	name2 = 'latex2mathprog/test/samples/extras/output/test'+str(num)+'.tex.mod'

	check_test(name1, name2)

def check_test_ampl_num(num, with_declarations = False):
	if with_declarations:
		name1 = 'latex2mathprog/test/samples/ampl/lp'+str(num)+'_ampl_with_declarations.tex.equation'
		name2 = 'latex2mathprog/test/samples/ampl/output/lp'+str(num)+'_ampl_with_declarations.tex.mod'
	else:
		name1 = 'latex2mathprog/test/samples/ampl/lp'+str(num)+'_ampl.tex.equation'
		name2 = 'latex2mathprog/test/samples/ampl/output/lp'+str(num)+'_ampl.tex.mod'

	check_test(name1, name2)


def test_lp0():
	check_test_num(0)

def test_lp0_with_declarations():
	check_test_num(0, True)

def test_lp1():
	check_test_num(1)

def test_lp1_with_declarations():
	check_test_num(1, True)

def test_lp2():
	check_test_num(2)

def test_lp2_with_declarations():
	check_test_num(2, True)

def test_lp3():
	check_test_num(3)

def test_lp3_with_declarations():
	check_test_num(3, True)

def test_lp4():
	check_test_num(4)

def test_lp4_with_declarations():
	check_test_num(4, True)

def test_lp5():
	check_test_num(5)

def test_lp5_with_declarations():
	check_test_num(5, True)

def test_lp6():
	check_test_num(6)

def test_lp6_with_declarations():
	check_test_num(6, True)

def test_lp7():
	check_test_num(7)

def test_lp7_with_declarations():
	check_test_num(7, True)

def test_lp8():
	check_test_num(8)

def test_lp8_with_declarations():
	check_test_num(8, True)

def test_lp9():
	check_test_num(9)

def test_lp9_with_declarations():
	check_test_num(9, True)



def test_lp10():
	check_test_num(10)

def test_lp10_with_declarations():
	check_test_num(10, True)

def test_lp11():
	check_test_num(11)

def test_lp11_with_declarations():
	check_test_num(11, True)

def test_lp12():
	check_test_num(12)

def test_lp12_with_declarations():
	check_test_num(12, True)

def test_lp13():
	check_test_num(13)

def test_lp13_with_declarations():
	check_test_num(13, True)

def test_lp14():
	check_test_num(14)

def test_lp14_with_declarations():
	check_test_num(14, True)

def test_lp15():
	check_test_num(15)

def test_lp15_with_declarations():
	check_test_num(15, True)

def test_lp16():
	check_test_num(16)

def test_lp16_with_declarations():
	check_test_num(16, True)

def test_lp17():
	check_test_num(17)

def test_lp17_with_declarations():
	check_test_num(17, True)

def test_lp18():
	check_test_num(18)

def test_lp18_with_declarations():
	check_test_num(18, True)

def test_lp19():
	check_test_num(19)

def test_lp19_with_declarations():
	check_test_num(19, True)



def test_lp20():
	check_test_num(20)

def test_lp20_with_declarations():
	check_test_num(20, True)

def test_lp21():
	check_test_num(21)

def test_lp21_with_declarations():
	check_test_num(21, True)

def test_lp22():
	check_test_num(22)

def test_lp22_with_declarations():
	check_test_num(22, True)

def test_lp23():
	check_test_num(23)

def test_lp23_with_declarations():
	check_test_num(23, True)

def test_lp24():
	check_test_num(24)

def test_lp24_with_declarations():
	check_test_num(24, True)

def test_lp25():
	check_test_num(25)

def test_lp25_with_declarations():
	check_test_num(25, True)

def test_lp26():
	check_test_num(26)

def test_lp26_with_declarations():
	check_test_num(26, True)

def test_lp27():
	check_test_num(27)

def test_lp27_with_declarations():
	check_test_num(27, True)

def test_lp28():
	check_test_num(28)

def test_lp28_with_declarations():
	check_test_num(28, True)

def test_lp29():
	check_test_num(29)

def test_lp29_with_declarations():
	check_test_num(29, True)


def test_lp30():
	check_test_num(30)

def test_lp30_with_declarations():
	check_test_num(30, True)

def test_lp31():
	check_test_num(31)

def test_lp31_with_declarations():
	check_test_num(31, True)

def test_lp32():
	check_test_num(32)

def test_lp32_with_declarations():
	check_test_num(32, True)

def test_lp33():
	check_test_num(33)

def test_lp33_with_declarations():
	check_test_num(33, True)

def test_lp34():
	check_test_num(34)

def test_lp34_with_declarations():
	check_test_num(34, True)

def test_lp35():
	check_test_num(35)

def test_lp35_with_declarations():
	check_test_num(35, True)

def test_lp36():
	check_test_num(36)

def test_lp36_with_declarations():
	check_test_num(36, True)

def test_lp37():
	check_test_num(37)

def test_lp37_with_declarations():
	check_test_num(37, True)

def test_lp38():
	check_test_num(38)

def test_lp38_with_declarations():
	check_test_num(38, True)

def test_lp39():
	check_test_num(39)

def test_lp39_with_declarations():
	check_test_num(39, True)


def test_lp40():
	check_test_num(40)

def test_lp40_with_declarations():
	check_test_num(40, True)

def test_lp41():
	check_test_num(41)

def test_lp41_with_declarations():
	check_test_num(41, True)

def test_lp42():
	check_test_num(42)

def test_lp42_with_declarations():
	check_test_num(42, True)

def test_lp43():
	check_test_num(43)

def test_lp43_with_declarations():
	check_test_num(43, True)

def test_lp44():
	check_test_num(44)

def test_lp44_with_declarations():
	check_test_num(44, True)

def test_lp45():
	check_test_num(45)

def test_lp45_with_declarations():
	check_test_num(45, True)

def test_lp46():
	check_test_num(46)

def test_lp46_with_declarations():
	check_test_num(46, True)

def test_lp47():
	check_test_num(47)

def test_lp47_with_declarations():
	check_test_num(47, True)

def test_lp48():
	check_test_num(48)

def test_lp48_with_declarations():
	check_test_num(48, True)

def test_lp49():
	check_test_num(49)

def test_lp49_with_declarations():
	check_test_num(49, True)


def test_lp50():
	check_test_num(50)

def test_lp50_with_declarations():
	check_test_num(50, True)

def test_lp51():
	check_test_num(51)

def test_lp51_with_declarations():
	check_test_num(51, True)

def test_lp52():
	check_test_num(52)

def test_lp52_with_declarations():
	check_test_num(52, True)

def test_lp53():
	check_test_num(53)

def test_lp53_with_declarations():
	check_test_num(53, True)

def test_lp54():
	check_test_num(54)

def test_lp54_with_declarations():
	check_test_num(54, True)

def test_lp55():
	check_test_num(55)

def test_lp55_with_declarations():
	check_test_num(55, True)

def test_lp56():
	check_test_num(56)

def test_lp56_with_declarations():
	check_test_num(56, True)

def test_lp57():
	check_test_num(57)

def test_lp57_with_declarations():
	check_test_num(57, True)

def test_lp58():
	check_test_num(58)

def test_lp58_with_declarations():
	check_test_num(58, True)

def test_lp59():
	check_test_num(59)

def test_lp59_with_declarations():
	check_test_num(59, True)


def test_lp60():
	check_test_num(60)

def test_lp60_with_declarations():
	check_test_num(60, True)

def test_lp61():
	check_test_num(61)

def test_lp61_with_declarations():
	check_test_num(61, True)

def test_lp62():
	check_test_num(62)

def test_lp62_with_declarations():
	check_test_num(62, True)

def test_lp63():
	check_test_num(63)

def test_lp63_with_declarations():
	check_test_num(63, True)

def test_lp64():
	check_test_num(64)

def test_lp64_with_declarations():
	check_test_num(64, True)

def test_lp65():
	check_test_num(65)

def test_lp65_with_declarations():
	check_test_num(65, True)

def test_lp66():
	check_test_num(66)

def test_lp66_with_declarations():
	check_test_num(66, True)

def test_lp67():
	check_test_num(67)

def test_lp67_with_declarations():
	check_test_num(67, True)

def test_lp68():
	check_test_num(68)

def test_lp68_with_declarations():
	check_test_num(68, True)

def test_lp69():
	check_test_num(69)

def test_lp69_with_declarations():
	check_test_num(69, True)


def test_lp70():
	check_test_num(70)

def test_lp70_with_declarations():
	check_test_num(70, True)

def test_lp71_with_declarations():
	check_test_num(71, True)

def test_lp72_with_declarations():
	check_test_num(72, True)

def test_lp73_with_declarations():
	check_test_num(73, True)

def test_lp74_with_declarations():
	check_test_num(74, True)

def test_lp75_with_declarations():
	check_test_num(75, True)

def test_lp76_with_declarations():
	check_test_num(76, True)


def test_extras_test1():
	check_test_extras_num(1)

def test_extras_test2():
	check_test_extras_num(2)

def test_extras_test3():
	check_test_extras_num(3)

def test_extras_test4():
	check_test_extras_num(4)

def test_extras_test5():
	check_test_extras_num(5)

def test_extras_test6():
	check_test_extras_num(6)

def test_extras_test7():
	check_test_extras_num(7)

def test_extras_test8():
	check_test_extras_num(8)

def test_extras_test9():
	check_test_extras_num(9)

def test_extras_test10():
	check_test_extras_num(10)

def test_extras_test11():
	check_test_extras_num(11)

def test_extras_test12():
	check_test_extras_num(12)

def test_extras_test13():
	check_test_extras_num(13)

def test_extras_test14():
	check_test_extras_num(14)

def test_extras_test15():
	check_test_extras_num(15)

def test_extras_test16():
	check_test_extras_num(16)

def test_extras_test17():
	check_test_extras_num(17)

def test_extras_test18():
	check_test_extras_num(18)

def test_extras_test19():
	check_test_extras_num(19)

def test_extras_test20():
	check_test_extras_num(20)

def test_extras_test21():
	check_test_extras_num(21)

def test_extras_test22():
	check_test_extras_num(22)

def test_extras_test23():
	check_test_extras_num(23)

def test_extras_test24():
	check_test_extras_num(24)

def test_extras_test25():
	check_test_extras_num(25)

def test_extras_test26():
	check_test_extras_num(26)

def test_extras_test27():
	check_test_extras_num(27)

def test_extras_test28():
	check_test_extras_num(28)

def test_extras_test29():
	check_test_extras_num(29)

def test_extras_test30():
	check_test_extras_num(30)

def test_extras_test31():
	check_test_extras_num(31)

def test_extras_test32():
	check_test_extras_num(32)

def test_extras_test33():
	check_test_extras_num(33)

def test_extras_test34():
	check_test_extras_num(34)

def test_extras_test35():
	check_test_extras_num(35)

def test_extras_test36():
	check_test_extras_num(36)

def test_extras_test37():
	check_test_extras_num(37)

def test_extras_test38():
	check_test_extras_num(38)

def test_extras_test39():
	check_test_extras_num(39)

def test_extras_test40():
	check_test_extras_num(40)

def test_extras_test41():
	check_test_extras_num(41)

def test_extras_test42():
	check_test_extras_num(42)

def test_extras_test43():
	check_test_extras_num(43)

def test_extras_test44():
	check_test_extras_num(44)

def test_extras_test45():
	check_test_extras_num(45)

def test_extras_test46():
	check_test_extras_num(46)

def test_extras_test47():
	check_test_extras_num(47)

def test_extras_test48():
	check_test_extras_num(48)

def test_extras_test49():
	check_test_extras_num(49)

def test_extras_test50():
	check_test_extras_num(50)

def test_extras_test51():
	check_test_extras_num(51)

def test_extras_test52():
	check_test_extras_num(52)

def test_extras_test53():
	check_test_extras_num(53)

def test_extras_test54():
	check_test_extras_num(54)

def test_extras_test55():
	check_test_extras_num(55)

def test_extras_test56():
	check_test_extras_num(56)

# AMPL samples
def test_lp0_ampl():
	check_test_ampl_num(0)

def test_lp1_ampl():
	check_test_ampl_num(1)

def test_lp2_ampl():
	check_test_ampl_num(2)

def test_lp3_ampl():
	check_test_ampl_num(3)

def test_lp4_ampl():
	check_test_ampl_num(4)

def test_lp5_ampl():
	check_test_ampl_num(5)

def test_lp6_ampl():
	check_test_ampl_num(6)

def test_lp7_ampl():
	check_test_ampl_num(7)

def test_lp8_ampl():
	check_test_ampl_num(8)

def test_lp9_ampl():
	check_test_ampl_num(9)

def test_lp10_ampl():
	check_test_ampl_num(10)

def test_lp11_ampl():
	check_test_ampl_num(11)

def test_lp12_ampl():
	check_test_ampl_num(12)

def test_lp13_ampl():
	check_test_ampl_num(13)

def test_lp14_ampl():
	check_test_ampl_num(14)

def test_lp15_ampl():
	check_test_ampl_num(15)

def test_lp16_ampl():
	check_test_ampl_num(16)

def test_lp17_ampl():
	check_test_ampl_num(17)

def test_lp18_ampl():
	check_test_ampl_num(18)

def test_lp19_ampl():
	check_test_ampl_num(19)

def test_lp20_ampl():
	check_test_ampl_num(20)

def test_lp21_ampl():
	check_test_ampl_num(21)

def test_lp22_ampl():
	check_test_ampl_num(22)

def test_lp23_ampl():
	check_test_ampl_num(23)

def test_lp24_ampl():
	check_test_ampl_num(24)

def test_lp25_ampl():
	check_test_ampl_num(25)

def test_lp26_ampl():
	check_test_ampl_num(26)

def test_lp27_ampl():
	check_test_ampl_num(27)

def test_lp28_ampl():
	check_test_ampl_num(28)

def test_lp29_ampl():
	check_test_ampl_num(29)

def test_lp31_ampl():
	check_test_ampl_num(31)

def test_lp32_ampl():
	check_test_ampl_num(32)

def test_lp33_ampl():
	check_test_ampl_num(33)

def test_lp34_ampl():
	check_test_ampl_num(34)

def test_lp35_ampl():
	check_test_ampl_num(35)

def test_lp36_ampl():
	check_test_ampl_num(36)

def test_lp37_ampl():
	check_test_ampl_num(37)

def test_lp38_ampl():
	check_test_ampl_num(38)

def test_lp39_ampl():
	check_test_ampl_num(39)

def test_lp40_ampl():
	check_test_ampl_num(40)

def test_lp41_ampl():
	check_test_ampl_num(41)

def test_lp42_ampl():
	check_test_ampl_num(42)

def test_lp44_ampl():
	check_test_ampl_num(44)

def test_lp45_ampl():
	check_test_ampl_num(45)

def test_lp46_ampl():
	check_test_ampl_num(46)

def test_lp47_ampl():
	check_test_ampl_num(47)

def test_lp48_ampl():
	check_test_ampl_num(48)

def test_lp49_ampl():
	check_test_ampl_num(49)

def test_lp50_ampl():
	check_test_ampl_num(50)

def test_lp51_ampl():
	check_test_ampl_num(51)
