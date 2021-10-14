#%% WSEN 01 02
'a' in {'a','b','c'}
3 in {0,1,2,3,4,5,6}
10 not in {0,1,2,3,4,5,6}
0 in {}
{1} in {{1}}

U = {0,1,2,3,4,5,6,7,8,9,10}
A = {2,3}
B = {1,2,3,4}

A.issubset(B)

for x in U:
    print(not (x in A) or (x in B))
    
{1,2,3} == {2,3,1}

X = set({})
for x in U:
    if x>2 and x<6:
        X.add(x)
    
print(X)

Y = set({})
for y in U:
    if y%2==0:
        Y.add(y)

print(Y)


[ x for x in U if x%2==0]

#%% Standard Model der Pyramide
Blue = {4}
White = {1,5,8}
Orange = {2,9}
Black = {0,3}
Green = {6,7,10}

X.union(Y)
Y.union(X)
Y.union(X) == X.union(Y)
X.intersection(Y)
Y.intersection(X)

for suit in ['S','H','D','C']:
    for rank in ['2','3','4','5','6','7','8','9','10','J','Q','K','A']: 
        print(suit,rank)

type([ x for x in U if x%2==0])
type({ x for x in U if x%2==0})


X.difference(Y)
Y.difference(X)