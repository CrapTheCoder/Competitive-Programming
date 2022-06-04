#include <bits/stdc++.h>
using namespace std;
 
int main(){
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int t; cin >> t;
 
    while(t--){
        string s; cin >> s;
 
        int l[4] = {-1, -1, -1, -1};
 
        int mini = INT_MAX;
 
        for(int i = 0; i < s.size(); i++){
            int cur = s[i] - '0';
 
            l[cur] = i;
 
            if(l[1] == -1 || l[2] == -1 || l[3] == -1)
                continue;
 
            if(cur == 1) mini = min(mini, i - min(l[2], l[3]) + 1);
            if(cur == 2) mini = min(mini, i - min(l[1], l[3]) + 1);
            if(cur == 3) mini = min(mini, i - min(l[1], l[2]) + 1);
        }
 
        cout << (mini == INT_MAX? 0 : mini) << "\n";
    }
}