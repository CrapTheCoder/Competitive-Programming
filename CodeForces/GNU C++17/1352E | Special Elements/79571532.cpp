#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

vector<bool> p(8000 * 8000, false);

int main()
{
ios::sync_with_stdio(false); cin.tie(NULL);

int t; cin >> t;

while(t--){
int n; cin >> n;
int a[n];

for(int i = 0; i < n; i++)
cin >> a[i];

for(int i = 0; i < n; i++){
int s = a[i];

for(int j = i+1; j < n; j++){
s += a[j];
p[s] = true;
}
}

int c = 0;

for(int i = 0; i < n; i++){
if(p[a[i]])
c++;
}

cout << c << endl;

for(int i = 0; i < n; i++){
int s = a[i];

for(int j = i+1; j < n; j++){
s += a[j];
p[s] = false;
}
}
}
}