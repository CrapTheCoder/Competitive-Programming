bits/stdc++.h>
namespace std;

int long long
endl '\n'

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

string maximum(int m, int s) {
string maxi;
(s - 9 >= 0) {
maxi.push_back('9');
-= 9;


!= 0)
maxi.push_back(s + '0');

(maxi.size() < m)
maxi.push_back('0');

maxi;


string minimum(int m, int s) {
string mini = "1";
;

string ending;
(s-9 >= 0) {
ending += "9";
-= 9;


!= 0)
ending = (char)(s + '0') + ending;

(mini.size() + ending.size() < m)
mini.push_back('0');

mini += ending;

if (mini.size() > m) {
return (char)((mini[0] - '0' + mini[1] - '0') + '0') + mini.substr(2, mini.size() - 2);
}

return mini;
}

signed main() {
ios::sync_with_stdio(false); cin.tie(NULL);

int m, s;
cin >> m >> s;

if (m == 1 && s == 0) {
cout << "0 0" << endl;
return 0;
}

if (s > m*9 || s < 1) {
cout << "-1 -1" << endl;
return 0;
}

cout << minimum(m, s) << " " << maximum(m, s) << endl;
}