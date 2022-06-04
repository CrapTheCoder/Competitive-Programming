#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;

int main(){
    string s, t; cin >> s >> t;

    int n = s.size(), m = t.size();

    int cnt = 0;

    for(int i = 0; i <= n - m; i++){
        string ns = "";

        for(int j = i; j < i + m; j++){
            ns += s[j];
        }

        if(ns == t)
            cnt++;
    }

    cout << cnt << endl;
}
