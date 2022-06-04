#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
#define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define INF 0x3f3f3f3f3f

int main() {

    fastio;

    ll n,m,a;
    priority_queue<ll> q;

    cin >> n >> m;
    for(ll i = 0; i < n+m; i++){

        cin >> a;
        if(a == -1){
            cout << q.top() << "\n";
            q.pop();
        }
        else q.push(a);
    }

    return 0;
}