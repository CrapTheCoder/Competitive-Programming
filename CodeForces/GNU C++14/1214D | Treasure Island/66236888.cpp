#include <iostream>
#include <random>
#include <ctime>

using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;

int main()
{
srand(time(0));

ll MODS[7] = {999996469, 999996407, 999996383, 999996359, 999996341, 999996329, 999996317};

ll MOD = MODS[rand() % 7];

ios::sync_with_stdio(false); cin.tie(0);

ll n, m; cin >> n >> m;

char l[n][m];

for(ll i = 0; i < n; i++){
for(ll j = 0; j < m; j++)
cin >> l[i][j];
}

if(m == 1){
for(ll i = 0; i < n; i++){
if(l[i][0] == '#'){
cout << 0;
return 0;
}
}

cout << 1;
return 0;
}

if(n == 1){
for(ll j = 0; j < m; j++){
if(l[0][j] == '#'){
cout << 0;
return 0;
}
}

cout << 1;
return 0;
}

ull dp1[n][m]; // Number of paths from (0, 0) to (i, j)
ull dp2[n][m]; // Number of paths from (i, j) to (n-1, m-1)

// Base cases
dp1[0][0] = 1;
dp2[n-1][m-1] = 1;

/////////////  dp1  /////////////

for(ll i = 1; i < n; i++){
if(l[i][0] == '#')
dp1[i][0] = 0;
else
dp1[i][0] = dp1[i-1][0];
}

for(ll j = 1; j < m; j++){
if(l[0][j] == '#')
dp1[0][j] = 0;
else
dp1[0][j] = dp1[0][j-1];
}

for(ll i = 1; i < n; i++){
for(ll j = 1; j < m; j++){
if(l[i][j] != '#')
dp1[i][j] = (dp1[i-1][j] + dp1[i][j-1]) % MOD;
else
dp1[i][j] = 0;
}
}


/////////////  dp2  /////////////

for(ll i = n-2; i >= 0; i--){
if(l[i][m-1] == '#')
dp2[i][m-1] = 0;
else
dp2[i][m-1] = dp2[i+1][m-1];
}

for(ll j = m-2; j >= 0; j--){
if(l[n-1][j] == '#')
dp2[n-1][j] = 0;
else
dp2[n-1][j] = dp2[n-1][j+1];
}

for(ll i = n-2; i >= 0; i--){
for(ll j = m-2; j >= 0; j--){
if(l[i][j] != '#')
dp2[i][j] = (dp2[i+1][j] + dp2[i][j+1]) % MOD;
else
dp2[i][j] = 0;
}
}

// No paths
if(dp2[0][0] == 0){
cout << 0;
return 0;
}

for(ll i = 0; i < n; i++){
for(ll j = 0; j < m; j++){
if((i == 0 && j == 0) || (i == n - 1 and j == m - 1))
continue;

if((dp1[i][j] * dp2[i][j]) % MOD == dp2[0][0]){
cout << 1;
return 0;
}
}
}

cout << 2;
}