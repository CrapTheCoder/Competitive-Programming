#include <iostream>
using namespace std;

/*

1 : Move left
2 : Move right
3 : Pick up box
4 : Drop box
0 : Quit

*/

int main()
{
    int r, c, i;
    int cur_row = 0;
    bool box_in_hand = false;
    cin >> r >> c;

    int s[r];

    for(i = 0; i < r; ++i) cin >> s[i];

    while(true){
        int cmd;
        cin >> cmd;

        if(cmd == 0){
            for(i = 0; i < r; ++i){
                cout << s[i];

                if(i != r - 1){
                    cout << " ";
                }
            }
            break;
        }

        if(cmd == 1){
            if(cur_row != 0){
                cur_row -= 1;
            }
        }

        if(cmd == 2){
            if(cur_row != (r - 1)){
                cur_row += 1;
            }
        }

        if(cmd == 3){
            if(s[cur_row] != 0 && !(box_in_hand)){
                s[cur_row] -= 1;
                box_in_hand = true;
            }
        }

        if(cmd == 4){
            if(s[cur_row] != c && box_in_hand){
                s[cur_row] += 1;
                box_in_hand = false;
            }
        }
    }
}