#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace std;
using namespace __gnu_pbds;

using int64 = int64_t;
using ld = long double;

template<typename T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;
template<typename T>
using ordered_multiset = tree<T, null_type, less_equal<T>, rb_tree_tag, tree_order_statistics_node_update>;

template<typename T>
using min_heap = priority_queue<T, vector<T>, greater<T>>;
template<typename T>
using max_heap = priority_queue<T, vector<T>, less<T>>;

namespace read {
    int Int() {
        int x;
        cin >> x;
        return x;
    }
    int64 Int64() {
        int64 x;
        cin >> x;
        return x;
    }
    char Char() {
        char c;
        cin >> c;
        return c;
    }
    string String() {
        string s;
        cin >> s;
        return s;
    }
    double Double() {
        return stod(String());
    }
    ld LongDouble() {
        return stold(String());
    }
    template<typename T1, typename T2>
    pair<T1, T2> Pair() {
        pair<T1, T2> p;
        cin >> p.first >> p.second;
        return p;
    }
    template<typename T>
    vector<T> Vec(const int n) {
        vector<T> v(n);
        for (T &x : v) {
            cin >> x;
        }
        return v;
    }
    template<typename T>
    vector<vector<T>> VecVec(const int n, const int m) {
        vector<vector<T>> v(n);
        for (vector<T> &vec : v) {
            vec = Vec<T>(m);
        }
        return v;
    }
}//namespace read

constexpr int kInf = 1e9 + 10;
constexpr int64 kInf64 = 1e15 + 10;
constexpr int kMod = 1e9 + 7;

inline void solution() {
    const int n = read::Int();
    vector<vector<int>> g(n);
    for (int i = 0; i < n - 1; i++) {
        const int x = read::Int() - 1, y = read::Int() - 1;
        g[x].push_back(y);
        g[y].push_back(x);
    }

    min_heap<pair<int, int>> q;
    q.push({0, -1});
    vector<int> series;

    while (not q.empty()) {
        const auto [x, p] = q.top();
        q.pop();
        for (const int y : g[x]) {
            if (y == p) continue;
            q.push({y, x});
        }
        series.push_back(x);
    }

    for (int i = 0; i < series.size(); i++) {
        cout << series[i] + 1;
        if (i != series.size()-1)
            cout << " ";
    }
    cout << '\n';
}

int32_t main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    // freopen(".in", "r", stdin);
    // freopen(".out", "w", stdout);

    cout << fixed << setprecision(10);

    int testcases = 1;
    //cin >> testcases;
    while (testcases--) {
        solution();
    }
}
