#include <bits/stdc++.h>
using namespace std;
 
#define endl '\n'
 
string f1(string text)
{
    string cop = text;
    int N = text.size();
    if(N == 0)
        return "";
    N = 2*N + 1; //Position count
    int L[N]; //LPS Length Array
    L[0] = 0;
    L[1] = 1;
    int C = 1; //centerPosition
    int R = 2; //centerRightPosition
    int i = 0; //currentRightPosition
    int iMirror; //currentLeftPosition
    int maxLPSLength = 0;
    int maxLPSCenterPosition = 0;
    int start = -1;
    int end = -1;
    int diff = -1;
 
    //Uncomment it to print LPS Length array
    //printf("%d %d ", L[0], L[1]);
    for (i = 2; i < N; i++)
    {
        //get currentLeftPosition iMirror for currentRightPosition i
        iMirror  = 2*C-i;
        L[i] = 0;
        diff = R - i;
        //If currentRightPosition i is within centerRightPosition R
        if(diff > 0)
            L[i] = min(L[iMirror], diff);
 
        //Attempt to expand palindrome centered at currentRightPosition i
        //Here for odd positions, we compare characters and
        //if match then increment LPS Length by ONE
        //If even position, we just increment LPS by ONE without
        //any character comparison
        while ( ((i + L[i]) < N && (i - L[i]) > 0) &&
            ( ((i + L[i] + 1) % 2 == 0) ||
            (text[(i + L[i] + 1)/2] == text[(i - L[i] - 1)/2] )))
        {
            L[i]++;
        }
 
        if(L[i] > maxLPSLength)  // Track maxLPSLength
        {
            maxLPSLength = L[i];
            maxLPSCenterPosition = i;
        }
 
        //If palindrome centered at currentRightPosition i
        //expand beyond centerRightPosition R,
        //adjust centerPosition C based on expanded palindrome.
        if (i + L[i] > R)
        {
            C = i;
            R = i + L[i];
        }
    }
    start = (maxLPSCenterPosition - maxLPSLength)/2;
    end = start + maxLPSLength - 1;
 
    int mx = 0;
 
    for(int i = 0; i < N / 2; i++)
        if(i - L[i] == 0)
            mx = L[i];
 
    string ans;
 
    for(int i = 0; i < mx; i++)
        ans += cop[i];
 
    return ans;
}
 
int main()
{
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int t; cin >> t;
 
    while(t--){
        string s; cin >> s;
        int n = s.size();
 
        string asd = s;
        reverse(asd.begin(), asd.end());
 
        if(s == asd){
            cout << s << endl;
            continue;
        }
 
        string tp = "";
        string ts = "";
 
        int i;
 
        for(i = 0; i < n / 2; i++){
            if(s[i] == s[n-i-1]){
                tp += s[i];
                ts += s[i];
            }
            else
                break;
        }
 
        reverse(ts.begin(), ts.end());
 
        string ns;
 
        for(int j = i; j <= n-i-1; j++)
            ns += s[j];
 
        string ns2 = ns;
        reverse(ns2.begin(), ns2.end());
 
        string x1 = f1(ns);
        string x2 = f1(ns2);
 
        string y1 = tp + ts;
        string y2 = tp + ts;
 
        string z1 = tp + x1 + ts;
        string z2 = tp + x2 + ts;
 
        if(z1.size() <= n) y1 = z1;
        if(z2.size() <= n) y2 = z2;
 
        if(y1.size() >= y2.size())
            cout << y1 << endl;
        else
            cout << y2 << endl;
    }
}