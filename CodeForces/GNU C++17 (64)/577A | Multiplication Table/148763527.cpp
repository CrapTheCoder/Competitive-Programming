#include<bits/stdc++.h>
 
using namespace std;
#define ll long long
 
int main() {
    ll n, x;
    cin >> n >> x;
 
    int c = 0;
    for (int i = 1; i <= sqrt(x); i++) {
        if (x % i == 0) {
            if (i > n || (x / i) > n)
                continue;
 
            c++;
            if (i != x / i)
                c++;
        }
    }
 
    cout << c << endl;
}