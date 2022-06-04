#include <iostream>
using namespace std;

int main() {
	int n; cin >> n;
	int c0 = 0, c1 = 0;
	
	for(int i = 0; i < n; i++){
	    int x;
	    cin >> x;
	    
	    if(x % 2 == 0) c0++;
	    if(x % 2 == 1) c1++;
	}
	
	if(abs(c0 - c1) <= 1)
	    cout << "DL" << endl;
	else
	    cout << "DETAIN" << endl;
	
	return 0;
}
