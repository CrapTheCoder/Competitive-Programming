#include <iostream>

using namespace std;

int add_digit(int n, int i){
return n * 10 + i;
}

int main()
{
int a, b, n;
cin >> a >> b >> n;

for(int i = 0; i <= 9; i++){
if(!(add_digit(a, i) % b)){
cout << a << i;

for(int x = 1; x < n; x++)
cout << 0;

cout << endl;

return 0;
}
}

cout << -1 << endl;
return 0;
}