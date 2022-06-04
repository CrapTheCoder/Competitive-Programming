#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;

int main(){
    int a, b; cin >> a >> b;

    if(a == 1 && b == 2) cout << 3 << endl;
    if(a == 1 && b == 3) cout << 2 << endl;
    if(a == 2 && b == 1) cout << 3 << endl;
    if(a == 2 && b == 3) cout << 1 << endl;
    if(a == 3 && b == 1) cout << 2 << endl;
    if(a == 3 && b == 2) cout << 1 << endl;
}
