obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}

obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}

def nestedEvenSum(obj, sum=0):
    # TODO
    for key in obj:
        if type(obj[key]) is dict:
            print("object")
            print(obj)
            print("key")
            print(key)
            print("key value")
            print(obj[key])
            sum+= nestedEvenSum(obj[key])
        elif type(obj[key]) is int and obj[key]%2==0:
            sum+= obj[key]
    return sum


nestedEvenSum(obj1)