#include <bits/stdc++.h>
using namespace std;

bool ispal(string s){
    for(int i = 0; i < s.size(); i++)
        if(s[i] != s[s.size() - i - 1])
            return false;

    return true;
}

int main(){
    int t; cin >> t;

    while(t--){
        string s; cin >> s;

        if(ispal(s))
            cout << 1;
        else
            cout << 2;

        cout << endl;
    }
}
