input0 = input()
input1 = input()
input2 = input()

meerkat = [input0, input1, input2]
meerkat[0], meerkat[2] = meerkat[2], meerkat[0]

print(meerkat)
