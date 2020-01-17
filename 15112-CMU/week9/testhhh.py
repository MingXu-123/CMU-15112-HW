def dfs(leftRemain, rightRemain, path, res):
    if leftRemain > rightRemain or leftRemain < 0 or rightRemain < 0:
        return  # backtracking
    if leftRemain == 0 and rightRemain == 0:
        res.append(path)
        return
    dfs(leftRemain - 1, rightRemain, path + "(", res)
    dfs(leftRemain, rightRemain - 1, path + ")", res)


# def generateParenthesis(n):
#     n = n/2
#     res = []
#     dfs(n, n, "", res)
#     return res

# print(generateParenthesis(6))

