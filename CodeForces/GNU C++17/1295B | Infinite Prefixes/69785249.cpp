#include <bits/stdc++.h>
using namespace std;

typedef int integer;
typedef long long int ll;

#define endl '\n'
#define int ll

integer main(){
ios::sync_with_stdio(false); cin.tie(NULL);

int t = 1;
cin >> t;

while(t--){
int n, x; cin >> n >> x;

string s; cin >> s;

int p0[n + 1]; p0[0] = 0;
int p1[n + 1]; p1[0] = 0;

for(int i = 1; i <= n; i++){
p0[i] = p0[i-1];
p1[i] = p1[i-1];

if(s[i-1] == '0') p0[i]++;
if(s[i-1] == '1') p1[i]++;
}

int p[n + 1];

for(int i = 0; i <= n; i++){
p[i] = p0[i] - p1[i];
}

if(p[n] == 0){
bool flag = false;

for(int i = 1; i <= n; i++){
if(p[i] == x){
flag = true;
break;
}
}

if(flag)
cout << -1 << endl;
else if(x == 0)
cout << 1 << endl;
else
cout << 0 << endl;

continue;
}

int c = 0;

for(int i = 1; i <= n; i++){
if((x - p[i]) % p[n] == 0 && (x - p[i]) / p[n] >= 0)
c++;
}

if(x == 0)
c++;

cout << c << endl;
}
}