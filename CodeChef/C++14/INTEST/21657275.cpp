#include <iostream>
using namespace std;

int main() {
	int n, k; cin >> n >> k;
	int c = 0;
	
	while(n--){
	    int i; cin >> i;
	    
	    if(i % k == 0)
	        c++;
	}
	
	cout << c << endl;
	
	return 0;
}
