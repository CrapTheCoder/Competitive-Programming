#include<bits/stdc++.h>
using namespace std;

int josephus(int n, int k)
{
  if (n == 1)
    return 1;
  else
    return (josephus(n - 1, k) + k-1) % n + 1;
}

int main(){
    int p = 2020;
    int n; cin >> n;

    cout << josephus(2020, n + 1);
}
