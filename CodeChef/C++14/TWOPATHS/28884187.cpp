#include <bits/stdc++.h>

using namespace std;
#define ll long long int
#define int ll
#define all int i=0; i<n; i++
#define T int t; cin>>t; while(t--)
#define INF 99999999999999999
int arr[1001][1001];
int pref[1001][1001];
int dpmax[1001][1001][21];
int dpmin[1001][1001][21];
int32_t main()
{
    //dpmax[i][j][k] = maximum sum path of length i(ending at ith row) ending at jth column, starting from (n, 0) with k up-left moves;
    //dpmin[i][j][k] = minimum sum path of length i(ending at ith row) ending at jth column, starting from (n, 0) with k up-left moves;
    T{
        int n,m,k;
        cin>>n>>m>>k;


        for(int i=0; i<=n; i++)pref[i][0] = 0;
        for(int j=0; j<=m; j++)pref[0][j] = 0;

        for(int j=0; j<=m; j++){
            for(int l=0; l<=k; l++)
                dpmin[0][j][l] = dpmax[0][j][l] = 0;
        }
        for(int i=0; i<=n; i++){
            for(int l=0; l<=k; l++)
                dpmin[i][0][l] = dpmax[i][0][l] = 0;
        }
        for(int i=1; i<=n; i++){
            for(int j=1; j<=m; j++){
                cin>>arr[i][j];
                if(j==1)pref[i][1] = arr[i][1];
                else pref[i][j] = pref[i][j-1] + arr[i][j];
            }
        }
        /*dpmin[1][1][1] = dpmax[1][1][1] = arr[1][1];

        for(int i=2; i<=m; i++){
            dpmax[1][i][1] = dpmin[1][i][1] = pref[1][i];
            //cout<<0<<" "<<i<<" "<<dpmin[0][i][0]<<endl;
        }
        for(int i=2; i<=m; i++){
            dpmax[i][1][1] = dpmin[i][1][1] = dpmin[i-1][1][1] + arr[i][1];
            //cout<<i<<" "<<0<<" "<<dpmin[i][0][0]<<endl;
        }*/

        for(int i=1; i<=n; i++){
            for(int j=1; j<=m; j++){
                for(int l=0; l<=k; l++){
                    if(l==0){
                        dpmax[i][j][l] = dpmax[i-1][j][l] + pref[i][j];
                        dpmin[i][j][l] = dpmin[i-1][j][l] + pref[i][j];
                    }
                    else{
                    dpmax[i][j][l] = max(dpmax[i-1][j-1][l-1], dpmax[i-1][j][l]) + pref[i][j];
                    dpmin[i][j][l] = min(dpmin[i-1][j-1][l-1], dpmin[i-1][j][l]) + pref[i][j];
                    }
                }
            }
        }

        int ans = -INF;
        int minarr[m+1], maxarr[m+1];

        fill(minarr, minarr + m + 1, INF);
        fill(maxarr, maxarr + m + 1, -INF);

        for(int j=0; j<=m; j++){
        for(int l=0; l<=k; l++){
            minarr[j] = min(minarr[j], dpmin[n][j][l]);
            maxarr[j] = max(maxarr[j], dpmax[n][j][l]);
        }
        }
        for(int i=0; i<m-k-1; i++){
            for(int j=i+k+2; j<m+1; j++){
                ans = max(ans, maxarr[j] - minarr[i]);
            }
        }

        cout<<ans<<endl;
       // cout<<maxarr[7] - minarr[2]<<endl;
    }
}
