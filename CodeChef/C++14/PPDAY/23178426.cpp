#include <bits/stdc++.h>
using namespace std;

int main(){
    int t; cin >> t;

    while(t--){
        int i;
        string s; cin >> s;

        for(i = 0; i < s.size(); i += 2){
            if(s[i] == s[i+1])
                {cout << "no" << endl; break;}
        }

        if(i == s.size())
            cout << "yes" << endl;
    }
}
