def emp_children(arr, child_age):
    result = []
    for emp in arr:
        for child in emp['children']:
            if child['age'] > child_age:
                result.append(emp['name'])
                break
    return result

ivan = {
    "name" : "ivan" ,
    "age" : 34 ,
    "children" : [{
        "name" : "vasja" ,
        "age" : 15 ,
    }, {
        "name" : "petja" ,
        "age" : 10 ,
    }],
}
darja = {
    "name" : "darja" ,
    "age" : 41 ,
    "children" : [{
        "name" : "kirill" ,
        "age" : 21 ,
    }, {
        "name" : "pavel" ,
        "age" : 15 ,
    }],
}
emps = [ivan , darja]

try_vivod = emp_children(emps, 18)
print('Искомые данные: ')
print(try_vivod)

