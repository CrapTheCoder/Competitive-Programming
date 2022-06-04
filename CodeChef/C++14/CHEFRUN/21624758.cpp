#include <iostream>

using namespace std;

int main()
{
    int test; cin >> test;

    while(test--){
        float x1, x2, x3;
        float v1, v2;

        cin >> x1 >> x2 >> x3;
        cin >> v1 >> v2;

        float t1 = (x3 - x1) / v1;
        float t2 = (x2 - x3) / v2;

        if(t1 == t2)
            cout << "Draw" << endl;
        if(t1 < t2)
            cout << "Chef" << endl;
        if(t1 > t2)
            cout << "Kefa" << endl;
    }
}
