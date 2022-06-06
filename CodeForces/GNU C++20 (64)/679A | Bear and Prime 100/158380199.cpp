bits/stdc++.h>
namespace std;

int long long

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

bool> queries;

(int value) {
value > 100)
return false;

queries.contains(value))
return queries[value];

<< value << endl;
string inp; cin >> inp;
queries[value] = (inp == "yes");


<int> ps = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47};

main() {
<int> a;
auto p: ps)
(query(p))
a.push_back(p);

size() == 0 || (a.size() == 1 && !query(a[0] * a[0])))
cout << "prime" << endl;

cout << "composite" << endl;
