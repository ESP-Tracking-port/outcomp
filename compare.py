import matplotlib.pyplot as plt

IN_A = "outsignal"
IN_B = "outfftfft"
CROP_LEFT = 200
CROP_RIGHT = 200
CB_STUB = lambda v: v
MULT_FACTOR = .25
SKIP_EVERY = 2
SKIP_EVERY_STARTFROM = 0


def filter_apply(lst, flt):
	for c in flt:
		lst = c(lst)

	return lst


def crop(l, left=CROP_LEFT, right=CROP_RIGHT):
	return l[left:-right]


def reverse(l):
	return list(reversed(l))


def mult(l, factor=MULT_FACTOR):
	return list(map(lambda i: i * factor, l))


def skip_every(l):
	lres = []

	for i in range(SKIP_EVERY_STARTFROM, len(l), SKIP_EVERY):
		print(i)
		lres.append(l[i])

	return lres


FILTER_COMMON_PRE = [
	CB_STUB,
	skip_every,
	crop,
]

FILTER_A = [
	CB_STUB,
]
FILTER_B = [
	CB_STUB,
	mult,
]
FILTER_X = [
	CB_STUB,
]


def main():
	with open(IN_A, 'r') as f:
		in_a = list(map(float, f.readlines()))

	with open(IN_B, 'r') as f:
		in_b = list(map(float, f.readlines()))

	x = list(range(len(in_b)))
	x = filter_apply(x, FILTER_COMMON_PRE)
	in_a = filter_apply(in_a, FILTER_COMMON_PRE)
	in_b = filter_apply(in_b, FILTER_COMMON_PRE)
	x = filter_apply(x, FILTER_X)
	in_a = filter_apply(in_a, FILTER_A)
	in_b = filter_apply(in_b, FILTER_B)
	plt.plot(x, in_a, label=IN_A)
	plt.plot(x, in_b, label=IN_B)
	plt.legend()
	plt.show()


if __name__ == "__main__":
	main()
