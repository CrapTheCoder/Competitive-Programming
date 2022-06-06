#include <bits/stdc++.h>
using namespace std;
 
#define endl '\n'
 
int main(){
    string s; cin >> s;
 
    if(s == "0"){
        cout << 0 << endl;
        return 0;
    }
 
    unsigned int n = s.size();
 
    reverse(s.begin(), s.end());
 
    int c = 0;
 
    for(unsigned int i = 0; i < n; i += 2)
        c++;
 
    if(n % 2 == 1 && count(s.begin(), s.end(), '1') == 1)
        c--;
 
    cout << c << endl;
}