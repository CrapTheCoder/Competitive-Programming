#include <iostream>

using namespace std;

int main()
{
    int n; cin >> n;
    int a[n];

    for(int i = 0; i < n; i++)
        cin >> a[i];

    for(int i = 0; i < n; i++){
        int j = i - 1;

        while(j >= 0 && a[j] > a[j+1]){
            swap(a[j], a[j+1]); j--;
        }

        cout << i - j << '\n';
    }
}
