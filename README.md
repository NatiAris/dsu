# dsu

DSU is a data structure that allows to effectively execute three operations:
- Add a new set (`make_sets`)
- Merge two sets (`union_sets`)
- Find the leader of the set to which an element belongs (`find_set`)

When used with rank heuristic and path compression heuristic, all three operations can be performed in almost constant time.

It looks something like that
```python
dsu = DSU(10)
for i in range(6,9):
    dsu.union_sets(i, i+1)
for i in range(4):
    dsu.union_sets(i, i+1)
dsu.find_set(1)  # 0
dsu.get_sets()  # {0: {0, 1, 2, 3, 4}, 5: {5}, 6: {6, 7, 8, 9}}
dsu  # [0, 0, 0, 0, 0, 5, 6, 6, 6, 6]
```

Note: the implementation presented is not intended to be very effective (arrays would likely work better than lists). Although, the asymptotic boost given by the implementation is sufficient to use it in coding challenges.

Note 2: don't use `compress` or `get_sets` in a loop, they are not efficient and not meant to. `compress` helps to ensure that all paths are minimal for cases when you want to check how many clusters you have at the moment. `get_sets` exists purely for representation purposes and implicitly performs the compression. Both operations are O(n).
