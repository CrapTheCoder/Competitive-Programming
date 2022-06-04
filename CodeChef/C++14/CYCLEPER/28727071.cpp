#include <bits/stdc++.h>
using namespace std;

typedef long long int ll;

string str(int n){
    string result = "";

    while(n > 0){
        result = (char)((n % 10) + '0') + result;
        n /= 10;
    }

    return result;
}

int main()
{
    int n; cin >> n;
    int a[n];

    for(int i = 0; i < n; i++){
        cin >> a[i]; a[i]--;
    }

    vector<string> anss;

    bool visited[n]; fill(visited, visited + n, false);

    for(int i = 0; i < n; i++){
        if(visited[i])
            continue;

        visited[i] = true;

        int current = i;

        string ans = "";

        while(a[current] != i){
            current = a[current];
            visited[current] = true;
            ans += str(current + 1) + " ";
        }

        anss.push_back(str(i + 1) + " " + ans + str(i + 1));
    }

    cout << anss.size() << endl;

    for(auto i: anss)
        cout << i << endl;
}
