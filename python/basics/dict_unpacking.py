# thought this was a neat way to access keys in a dictionary. Deservers futher exploration.

d = {"k1": 10, "k2": [1, 2, 3], "k3": {"a": 10, "b": 12, "c": 23}}

new = {"k1": 1, **d}

print(new)
