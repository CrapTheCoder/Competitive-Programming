#include <bits/stdc++.h>
#include <iostream>
#include <vector>

using namespace std;

#define MOD 1000000007

int main()
{
    ios_base::sync_with_stdio(false);cin.tie(NULL);

    int t; cin>>t;

    while(t--){
        long long int n,d=0,p=0;
        vector<long long int> prices;
        cin>>n;
        for(long long int i=0; i<n; i++){
            int b;
            cin>>b;
            prices.push_back(b);
        }

        sort(prices.begin(),prices.end(),greater<int>());

        for(long long int j=0; j<n; j++){
                    if(prices[j]-d>0){
                        p+=prices[j]-d;
                        p %= MOD;
                    }
                    d++;
        }

        cout<<p<<endl;
    }
}
