#include <iostream>
using namespace std;

int main() {
    int x; float y;
	cin >> x >> y;
	
	if((y >= x + 0.5) && (x % 5 == 0))
	    y -= x + 0.5;
	
	cout << y << endl;
}
