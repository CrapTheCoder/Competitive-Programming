#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

#define MAX 1000020

int pre[MAX + 2];
bool prime[MAX + 2];
vector<int> ps;

void sieve() {
int p = 2;
while (p * p < MAX) {
if (prime[p])
for (int i = p*p; i < MAX; i += p)
prime[i] = false;

p++;
}

for (int p = 2; p < MAX; p++)
if (prime[p])
ps.emplace_back(p);
}

signed main() {
ios::sync_with_stdio(false); cin.tie(NULL);

fill(prime, prime + MAX, true);
sieve();

int cur = 0;
int curl = 0;
int sq = 0;

for (int n = 1; n <= 1000003; n++) {
if (n >= ps[cur])
cur++;

while ((sq+1) * (sq+1) <= n)
sq++;

while (ps[curl] <= sq)
curl++;

pre[n] = cur - curl + 1;
}

int tcs; cin >> tcs;

while(tcs--) {
int n; cin >> n;
cout << pre[n] << endl;
}
}