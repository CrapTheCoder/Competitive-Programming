#include <bits/stdc++.h>

using namespace std;

void int_input(int &n){
    n = 0;

    register char c = getchar();

    bool neg = false;

    if(c == '-'){
        neg = true;
        c = getchar();
    }

    for(; '0' <= c && c <= '9'; c = getchar()){
        n = n * 10 + c - '0';
    }

    if(neg)
        n = -n;
}

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    
    int n; int_input(n);

    int a[n];

    for(int i = 0; i < n; i++)
        int_input(a[i]);

    int max_now = -1;

    for(int i = 0; i < n; i++)
        max_now = max(max_now, 1 + i + a[i]);

    int ans[n] = {0}; ans[0] = max_now;

    for(int i = 0; i < n - 1; i++){
        max_now = max(max_now - 1, a[i] + n);
        ans[n - i - 1] = max_now;
    }

    for(int i = 0; i < n; i++)
        cout << ans[i] << " ";
}
