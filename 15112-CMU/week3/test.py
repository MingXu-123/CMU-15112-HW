s = """\
We hold these truths to be
self-evident: that all men are
created equal; that they are
endowed by their Creator with
certain unalienable rights;
that among these are life,
liberty, and the pursuit of
happiness."""

L = s.split('\n')
print(L)
res = ""
for line in L:
    blanks = 30 - len(line)
    res += (" " * blanks + line + '\n')
print(res)


text = "dadadffe"
i = 1
print(text[:i] + "\n" + text[i+1:])


# a = "fujian     xuming     ruicheng zuowei         guofu"
#
# s = a.split()
#
# print(" ".join(s))
#
# text = """\
# We hold these truths to be self-evident:  that all men are created equal;
# that they are endowed by their Creator with certain unalienable rights;
# that among these are life, liberty, and the pursuit of happiness."""
#
# element = text.split()
#
# print(" ".join(element))