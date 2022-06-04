#include <iostream>
 
#define ll long long
 
using namespace std;
 
int main(){
 
    int t;cin>>t;while(t--){
        ll n; cin>>n;
 
        if (n % 2 == 1 || n < 4) {
            cout << -1 << endl;
            continue;
        }
 
        ll mini = n/6;
        if (n % 6 == 2 || n % 6 == 4)
            mini++;
 
        ll maxi = n/4;
 
        cout << mini << " " << maxi << endl;
    }
 
    return 0;
}