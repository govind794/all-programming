import collections

d1 = {"a":1, "b":{"m":1}}
d2 = {"c":3, "d":4}
d3 = {"e":5, "f":6}

chain = collections.ChainMap(d1, d2, d3)

# print(chain.maps)

# print(list(chain.keys()))
print(list(chain.values()))
