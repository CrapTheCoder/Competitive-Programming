#include <bits/stdc++.h>
using namespace std;

void get_array(int a[], int n){
    for(int i = 0; i < n; i++)
        cin >> a[i];
}

int main()
{
    int test; cin >> test;

    while(test--){
        int c = 0;

        int n, k; cin >> n >> k;
        int a[n]; get_array(a, n);

        sort(a, a + n, greater<int>());
        int pass_mark = a[k-1];

        for(int i = 0; i < n; i++){
            if(a[i] >= pass_mark)
                c++;
            else
                break;
        }

        cout << c << endl;
    }
}
