#include <bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n; cin >> n;

    int a[n];

    for(int i = 0; i < n; i++)
        cin >> a[i];

    sort(a, a + n);

    int c = 0;

    for(int i = 1; i < n; i++)
        if(a[i] != a[i - 1])
            c++;

    cout << c << endl;
}
