def check_balanced(p, up):
    if len(up) == 0:
        return True

    if up[0] == "(" or up[0] == "{" or up[0] == "[":
        return check_balanced(p + up[0], up[1:])
    else:
        if p[-1] + up[0] == "()" or p[-1] + up[0] == "[]" or p[-1] + up[0] == "{}":
            return check_balanced(p[:-1], up[1:])
        else:
            return False

# str="[()]{}{[()()]()}"
str="[(])"
print(check_balanced("",str))
