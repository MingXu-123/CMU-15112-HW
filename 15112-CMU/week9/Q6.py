def generateValidParentheses(n):
    pass

def testGenerateValidParentheses():
    print("Testing generateValidParentheses...", end="")
    assert(generateValidParentheses(4) == { "(())", "()()" })
    assert(generateValidParentheses(6) == { "((()))", "()(())", "(())()", "(()())", "()()()" })
    assert(generateValidParentheses(5) == set())
    assert(generateValidParentheses(0) == set())
    print("Passed!")


# print(checkStr("(())"))
# print(checkStr("())("))
# print(checkStr(")()("))
# print(generateValidParentheses(4))
# print(generateValidParentheses(6))
# print(generateValidParentheses(5))
# print(generateValidParentheses(0))

def print_all_parens(n):
    def print_parens(left, right, s):
        if right == n/2:
            print(s)
            return
        if left < n/2:
            print_parens(left + 1, right, s + "(")
        if right < left:
            print_parens(left, right + 1, s + ")")

    print_parens(0, 0, "")

print(print_all_parens(6))





class Solution(object):
    def generateParenthesis(self, n):
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans

def generateParenthesis(n):
    def generate(A = []):
        if len(A) == n:
            if valid(A):
                ans.append("".join(A))
        else:
            A.append('(')
            generate(A)
            A.pop()
            A.append(')')
            generate(A)
            A.pop()

    def valid(A):
        bal = 0
        for c in A:
            if c == '(':
                bal += 1
            else: bal -= 1
            if bal < 0:
                return False
        return bal == 0

    ans = []
    generate()
    return ans

# print(generateParenthesis(6))