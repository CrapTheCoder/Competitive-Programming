#include<bits/stdc++.h>
using namespace std;

#define ll long long int

ll gcd(ll a, ll b){
    while(b != 0){
        ll temp = a % b;
        a = b;
        b = temp;
    }

    return a;
}

ll lcm(ll a, ll b){
    return (a * b) / gcd(a, b);
}

int main()
{
    ll n, m; cin >> n >> m;

    cout << lcm(n, m);
}
