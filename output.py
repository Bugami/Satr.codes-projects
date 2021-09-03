def postFix(expr):
    vals = expr.split(' ')
    for i in vals:
        try:
            int(i)
        except ValueError:
            val1 = vals[vals.index(i)-2]
            val2 = vals[vals.index(i)-1]
            if i == '+':
                result = int(val1) + int(val2)
                vals = vals[vals.index(i)+1:]
                vals.insert(0,result)
            elif i == '-':
                result = int(val1) - int(val2)
                vals = vals[vals.index(i)+1:]
                vals.insert(0,result)
            elif i == '*':
                result = int(val1) * int(val2)
                vals = vals[vals.index(i)+1:]
                vals.insert(0,result)
            elif i == '/':
                result = int(val1) / int(val2)
                vals = vals[vals.index(i)+1:]
                vals.insert(0,result)
    return vals[0]

list1 = '4 1 - 2 *'
print(postFix(list1))