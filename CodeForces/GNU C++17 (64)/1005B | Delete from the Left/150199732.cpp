bits/stdc++.h>
namespace std;

int long long
endl '\n'

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

main() {
sync_with_stdio(false); cin.tie(NULL);

string s, t;
s >> t;

index1 = s.size() - 1;
index2 = t.size() - 1;

longest_suffix = 0;
(index1 >= 0 && index2 >= 0 && s[index1] == t[index2]) {
longest_suffix++;
index1--;
index2--;


<< (s.size() - longest_suffix) + (t.size() - longest_suffix) << endl;
