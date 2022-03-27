# dic = {"name": {"govind": "patidar"}}
# print(dic.get("name"))
# print(dic.get("govind", "Not Found"))
# print(dic["name1"])


# dic.setdefault("name1", "Not found")
# print(dic.get("name1"))

import collections

dic = collections.defaultdict(lambda : "Key not found")

dic["name"] = "govind"
dic["sername"] = "patidar"

print(dic.get("name"))
print(dic["job"])


