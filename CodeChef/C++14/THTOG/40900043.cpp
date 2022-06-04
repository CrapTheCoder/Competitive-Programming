#include <bits/stdc++.h>
using namespace std;

long long p3(long long x){
    long long counter=0;
    while (x % 3 == 0){
        x /= 3;
        counter++;
    }
    return counter;
}

int main(){
    long long n;
    vector<pair<long long,long long> > vals;
    cin >> n;

    for (long long i=0; i<n; i++){
        pair<long long, long long> x;
        cin >> x.second;
        x.first -= p3(x.second);
        vals.push_back(x);
    }

    sort(vals.begin(), vals.end());

    for (long long i=0; i<n; i++) {
        cout << vals[i].second << ' ';
    }
}
