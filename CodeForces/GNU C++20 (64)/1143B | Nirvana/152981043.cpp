bits/stdc++.h>
namespace std;

int long long
endl '\n'

main() {
sync_with_stdio(false); cin.tie(NULL);

string s; cin >> s;

= 1, maxi = pow(9, s.size() - 1);
int i = 0; i < s.size(); i++) {
(s[i] != '0') {
int nw = f * (s[i]-'0'-1) * pow(9, s.size()-i-1);
if (maxi < nw) maxi = nw;


*= s[i]-'0';


<< max(maxi, f) << endl;
