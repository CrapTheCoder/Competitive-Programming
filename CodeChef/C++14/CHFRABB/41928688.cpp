#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'
#define INF INT_MAX
/* C++ program to find the minimum number of jumps to reach the end of an array */
#include<bits/stdc++.h>
#include<vector>
using namespace std;

int jumps(vector<int> &A)
{
	if(A.size()<=1)
    	return 0;
	if(A[0]==0)
    	return -1;
	int n = A.size();
	int jumps = 1;
	int reachable = 0;
	int curr = A[0];
	for(int i=1;i<n;i++)
	{
    	reachable = max(reachable, i+A[i]);
    	if(curr==i && i!=n-1)
    	{
        	jumps++;
        	curr = reachable;
        	reachable = -1;
    	}
    	if(curr==i && i!=n-1)
        	return -1;
	}
	return jumps;
}

signed main()
{
    ios::sync_with_stdio(false); cin.tie(NULL);

    int t; cin >> t;

    while (t--) {
        int n; cin >> n;

        vector<int> a(n);
        for (int i = 0; i < n; i++)
            cin >> a[i];

        cout << jumps(a) << endl;
    }
}
