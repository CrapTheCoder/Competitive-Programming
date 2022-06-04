#include <bits/stdc++.h>
#define inar ll ar[n];for(ll i=0;i<n;i++) cin>>ar[i];
#define loop for(ll i=0;i<n;i++)
#define fast ios_base::sync_with_stdio(0); cin.tie(NULL);
#define endl "\n"
#define mod int(1e9 +7)

typedef long long int ll;
using namespace std;

#define INFI LLONG_MAX
int32_t main()
{
	ll t; cin>>t;

	while(t--)
	{
		ll n; cin >> n;
		ll k; cin >> k;

		ll ar[n];

		ll sum = 0;

		for(ll i=0;i<n;i++){
		    cin >> ar[i];
            sum += ar[i];
        }

        sort(ar, ar + n);

        ll ans1 = 0;

        for(ll i = 0; i < k; i++)
            ans1 += ar[i];

        ll ans2 = 0;

        for(ll i = n - 1; i > n - k - 1; i--)
            ans2 += ar[i];

        ll val1 = max(sum - ans1, ans1) - min(sum - ans1, ans1);
        ll val2 = max(sum - ans2, ans2) - min(sum - ans2, ans2);

        cout<<max(val1,val2)<<endl;
    }
}
