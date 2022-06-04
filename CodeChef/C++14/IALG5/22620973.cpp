#include <bits/stdc++.h>
using namespace std;

int main(){
	int n, k, r; cin >> n >> k >> r;
	int s = k / r;
	int x = (-1.0 + sqrt(1.0 + 8.0 * s)) / 2.0;
	
	cout << n - x << endl;
}