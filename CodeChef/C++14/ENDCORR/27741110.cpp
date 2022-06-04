#include <bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
using namespace std;

int binSearch(int n, vector<int> a, int x){
    int l = 0, r = n - 1;

    while(l < r){
        int m = (l + r) / 2;

        if(a[m] == x) return m;
        if(a[m] < x) l = m + 1;
        if(a[m] > x) r = m;
    }

    if(a[l] < x)
        return l + 1;

    return l;
}

void printVect(vector<int> v, int n){
    for(int i = 0; i < n; i++)
        cout << v[i] << ' ';
    cout << endl;
}

int main()
{
    fastio;
	int n, m; cin >> n >> m;

	int l = 0;
	vector<int> a;

	for(int i = 0; i < n+m; i++){
        int x; cin >> x;

        if(x == -1){
            if(l > 0){
                cout << a[l-1] << endl;
                l--;
                a.pop_back();
            }
        }

        else {
            if(l == 0){
                a.push_back(x);
                l++;
            }

            else {
                a.insert(a.begin() + binSearch(l, a, x), x);
                l++;
            }
        }
	}
}

