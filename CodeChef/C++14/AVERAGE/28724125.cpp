#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n; cin >> n;

    unordered_map<int, int> mapped;

    int a[n];

    for(int i = 0; i < n; i++){
        cin >> a[i];

        mapped[a[i]]++;
    }

    int ans = 0;

    for(int i = 0; i < n; i++){
        for(int j = i + 1; j < n; j++){
            int avg = a[i] + a[j];

            if(avg % 2)
                continue;

            avg /= 2;

            if(mapped.count(avg)){
                ans += mapped[avg];
                mapped.erase(avg);
            }
        }
    }

    cout << ans << '\n';
}
