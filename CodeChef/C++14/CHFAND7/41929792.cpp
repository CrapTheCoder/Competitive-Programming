#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'
#define INF INT_MAX

int count2sinRangeAtDigit(int number, int d)
{
    int powerOf10 = (int)pow(10, d);
    int nextPowerOf10 = powerOf10 * 10;
    int right = number % powerOf10;

    int roundDown = number - number % nextPowerOf10;
    int roundup = roundDown + nextPowerOf10;

    int digit = (number / powerOf10) % 10;

    if (digit < 7)
        return roundDown / 10;

    if (digit == 7)
        return roundDown / 10 + right + 1;

    return roundup / 10;
}

int numberOf2sinRange(int number)
{
    stringstream convert;
    convert << number;
    string s = convert.str();
    int len = s.length();

    int count = 0;
    for (int digit = 0; digit < len; digit++)
        count += count2sinRangeAtDigit(number, digit);

    return count;
}

signed main()
{
    ios::sync_with_stdio(false); cin.tie(NULL);

    int t; cin >> t;

    while (t--) {
        int l, r; cin >> l >> r;
        cout << numberOf2sinRange(r) - numberOf2sinRange(l-1) << endl;
    }
}
