#include <bits/stdc++.h>
using namespace std;

int n;
int a[100000];
int p[100000];
int m[100000];

vector<int> gr[100000];

int solve(int u){
    int mini = a[u];

    for(auto v: gr[u]){
        mini = min(mini, solve(v));
    }

    return m[u] = mini;
}

int main(){
    cin >> n;

    for(int i = 0; i < n; i++) cin >> a[i];
    for(int i = 0; i < n; i++) cin >> p[i];

    int root;

    for(int i = 0; i < n; i++){
        if(p[i] != -1)
            gr[p[i] - 1].push_back(i);
        else
            root = i;
    }

    solve(root);

    int maxi = INT_MIN;

    for(int i = 0; i < n; i++)
        maxi = max(maxi, a[i] - m[i]);

    cout << maxi << endl;
}
