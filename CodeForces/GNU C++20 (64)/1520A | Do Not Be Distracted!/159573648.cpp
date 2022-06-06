bits/stdc++.h>
namespace std;

endl '\n'
int long long

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

main() {
sync_with_stdio(false); cin.tie(NULL);

; cin >> tc;
(tc--) {
int n; cin >> n;
string s; cin >> s;

// First occurrence
vector<int> fo(26, -1);
for (int i = 0; i < n; i++)
if (fo[s[i] - 'A'] == -1)
fo[s[i] - 'A'] = i;

// Last occurrence
vector<int> lo(26, -1);
for (int i = n-1; i >= 0; i--)
if (lo[s[i] - 'A'] == -1)
lo[s[i] - 'A'] = i;

bool flag = false;  // Denotes whether he got distracted or not
for (int i = 0; i < 26; i++) {
if (fo[i] == -1)
continue;

// For each occurrence from first to last check if all characters are same
for (int j = fo[i]; j <= lo[i]; j++)
if (s[j] - 'A' != i)
flag = true;


// Final output
if (!flag)
cout << "YES" << endl;
else
cout << "NO" << endl;
}
}