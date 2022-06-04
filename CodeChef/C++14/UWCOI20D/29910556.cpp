///*** AUTHOR: SRIVATHS P (crap_the_coder) ***///

#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    
    int t; cin >> t;

    while(t--){
        // Contains all the pairs of (i, j) where a[i][j] = 1
        vector<pair<int, int>> v;

        int n; cin >> n;

        char a[n][n];

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                cin >> a[i][j];

                if(a[i][j] == '1')
                    v.push_back({i, j});
            }
        }

        int answer = 0;

        for(int i = 0; i < v.size(); i++){
            // We are assuming (0, 0) is the top left corner
            int r_left = 0; // The topmost row index within a square (Always 0, just added it for more clarity)
            int r_right = 0; // The bottommost row index within a square

            int c_left = 0; // The leftmost column within a square (Can be negative)
            int c_right = 0; // The rightmost column within a square

            /// NOTE: A negative c_left means a column is to the left
            /// For example, [(1, 2), (2, 1)] would yield a negative value as (2, 1) is to the left of (1, 2)

            for(int j = i; j < v.size(); j++){
                if(v[j].first - v[i].first < r_left) r_left = v[j].first - v[i].first;
                if(v[j].first - v[i].first > r_right) r_right = v[j].first - v[i].first;

                if(v[j].second - v[i].second < c_left) c_left = v[j].second - v[i].second;
                if(v[j].second - v[i].second > c_right) c_right = v[j].second - v[i].second;

                /// For a set of coordinates to be within a square,
                /// It's required that differences of any pair <= length of square
                /// Here, the differences between the leftmost value and the rightmost values would do the trick

                if(abs(r_right - r_left) <= j - i && abs(c_right - c_left) <= j - i)
                    answer++;
            }
        }

        cout << answer << endl;
    }
}
