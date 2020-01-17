def replaceWhiteSpace(text):
    element = text.split()
    newText = " ".join(element)
    return newText


def rightJustifyText(text, width):
    text = replaceWhiteSpace(text)
    lenOfStr = len(text)
    i = width
    judgeIndex = i
    while judgeIndex < lenOfStr:
        if text[i] == " ":
            text = text[:i] + "\n" + text[i + 1:]
            judgeIndex = i + width + 1
            i = judgeIndex
        else:
            while text[i] != " ":
                i -= 1
                if text[i] == " ":
                    text = text[:i] + "\n" + text[i + 1:]
                    judgeIndex = i + width + 1
                    i = judgeIndex
                    if judgeIndex > lenOfStr - 1:
                        break
    lines = text.split('\n')
    result = ""
    for line in lines:
        spaces = width - len(line)
        if lines.index(line) != len(lines) - 1:
            result += (" " * spaces + line + "\n")
        else:
            result += (" " * spaces + line)
    return result




def testRightJustifyText():
    print("Testing rightJustifyText()...", end="")
    text1 = """\
We hold these truths to be self-evident:  that all men are created equal;
that they are endowed by their Creator with certain unalienable rights;
that among these are life, liberty, and the pursuit of happiness."""
    text1Result = """\
    We hold these truths to be
self-evident: that all men are
  created equal; that they are
 endowed by their Creator with
   certain unalienable rights;
    that among these are life,
   liberty, and the pursuit of
                    happiness."""
    assert(rightJustifyText(text1, 30) == text1Result)

# testRightJustifyText()


# rightJustifyText(text, 20)
text1 = """\
We hold these truths to be self-evident:  that all men are created equal;
that they are endowed by their Creator with certain unalienable rights;
that among these are life, liberty, and the pursuit of happiness."""

text1Result = """\
    We hold these truths to be
self-evident: that all men are
  created equal; that they are
 endowed by their Creator with
   certain unalienable rights;
    that among these are life,
   liberty, and the pursuit of
                    happiness."""

text2 = """\
Though, in reviewing the incidents of my administration,
I am unconscious of intentional error, I am nevertheless too sensible of my
defects not to think it probable that I may have committed many errors.
I shall also carry with me the hope that my country will view them with
indulgence; and that after forty-five years of my life dedicated to its service
with an upright zeal, the faults of incompetent abilities will be consigned to
oblivion, as I myself must soon be to the mansions of rest.

I anticipate with pleasing expectation that retreat in which I promise myself
to realize the sweet enjoyment of partaking, in the midst of my fellow-citizens,
the benign influence of good laws under a free government,
the ever-favorite object of my heart, and the happy reward,
as I trust, of our mutual cares, labors, and dangers."""
text2Result = """\
         Though, in reviewing the incidents of my administration, I am
unconscious of intentional error, I am nevertheless too sensible of my
       defects not to think it probable that I may have committed many
 errors. I shall also carry with me the hope that my country will view
      them with indulgence; and that after forty-five years of my life
          dedicated to its service with an upright zeal, the faults of
 incompetent abilities will be consigned to oblivion, as I myself must
           soon be to the mansions of rest. I anticipate with pleasing
     expectation that retreat in which I promise myself to realize the
 sweet enjoyment of partaking, in the midst of my fellow-citizens, the
            benign influence of good laws under a free government, the
ever-favorite object of my heart, and the happy reward, as I trust, of
                                our mutual cares, labors, and dangers."""
# print(rightJustifyText(text2, 70))
print(rightJustifyText(text1, 30))
# print(text1Result)
print(repr(rightJustifyText(text1, 30)))
print(repr(text1Result))
print(rightJustifyText(text1, 30) == text1Result)

