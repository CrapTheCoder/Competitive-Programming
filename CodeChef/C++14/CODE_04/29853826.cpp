#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define speed ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

int lcs(string X, string Y, int m, int n){
	int L[m + 1][n + 1];
	int i, j;

	for (i = 0; i <= m; i++) {
		for (j = 0; j <= n; j++){
		if (i == 0 || j == 0)
			L[i][j] = 0;

		else if (X[i - 1] == Y[j - 1])
			L[i][j] = L[i - 1][j - 1] + 1;

		else
			L[i][j] = max(L[i - 1][j], L[i][j - 1]);
		}
	}

	return L[m][n];
}

int main(){
    speed;

    string s1, s2; cin >> s1 >> s2;

    cout << lcs(s1, s2, s1.size(), s2.size()) << endl;
}
