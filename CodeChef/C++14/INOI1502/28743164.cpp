#include <bits/stdc++.h>
using namespace std;

typedef long long int ll;

ll n, MOD;

vector<ll> divisors(ll n)
{
    vector<ll> d = {1};

    for(ll i = 2; i <= sqrt(n); i++)
    {
        if(n % i == 0)
        {
            if (i == (n / i))
                d.push_back(i);
            else {
                d.push_back(i);
                d.push_back(n / i);
            }
        }
    }

    return d;
}

int power(ll x, ll y)
{
    int res = 1;

    x %= MOD;

    while (y > 0)
    {
        if (y & 1)
            res = (res*x) % MOD;

        y >>= 1;
        x = (x * x) % MOD;
    }

    return res;
}

ll solve(ll n){
    if(n == 1)
        return 2;

    ll answer = power(2, n);

    for(auto i: divisors(n)){
        answer -= solve(i);

        if(answer < 0){
            answer %= MOD;
            answer = MOD + answer;
        }

        else
            answer %= MOD;

    }

    return answer % MOD;
}

int main()
{
    cin >> n >> MOD;

    cout << solve(n) << endl;
}