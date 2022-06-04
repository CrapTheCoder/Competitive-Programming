#include <bits/stdc++.h>

using namespace std;

int main(){
    int n; cin >> n;

    vector<int> a;

    for(int i = 0; i < n; i++){
        int val; cin >> val;

        a.insert(a.begin() + (i - val), i + 1);
    }

    for(int i: a)
        cout << i << " ";

    cout << endl;
}
