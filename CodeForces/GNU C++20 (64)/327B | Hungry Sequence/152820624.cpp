bits/stdc++.h>
namespace std;

int long long
endl '\n'

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

MAX = 10000013;
[MAX];

main() {
sync_with_stdio(false); cin.tie(NULL);

cin >> n;

sieve, sieve+MAX, true);

cnt = 0;
0] = sieve[1] = false;
int i = 2; i < MAX; i++) {
(!sieve[i])
continue;

cnt++;
cout << i << " ";

(cnt == n)
break;

for (int j = i*i; j < MAX; j += i)
sieve[j] = false;


<< endl;
