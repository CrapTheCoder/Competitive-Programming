#include <bits/stdc++.h>
using namespace std;

typedef int integer;
typedef long long int ll;

#define int ll
#define endl '\n'

#define INF LLONG_MAX

#define HASH 1000000007

int hasher(int x, int y){
return x * HASH + y;
}

pair<int, int> unhasher(int x){
return {x / HASH, x % HASH};
}

integer main()
{
int t; cin >> t;

while(t--){
int n; cin >> n;
string s; cin >> s;

int x = 0;
int y = 0;

unordered_map<int, int> d;

d[0] = 0;

int m = INF;
int mi = -1;

for(int i = 0; i < n; i++){
if(s[i] == 'L') x--;
if(s[i] == 'R') x++;

if(s[i] == 'U') y++;
if(s[i] == 'D') y--;

int z = hasher(x, y);

if(d.count(z)){
if(m > (i + 1) - d[z]){
m = (i + 1) - d[z];
mi = i + 1;
}
}

d[z] = i + 1;
}

if(mi == -1)
cout << -1 << endl;
else
cout << mi - m + 1 << " " << mi << endl;
}
}