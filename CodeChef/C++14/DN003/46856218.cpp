// CPP program to find number switch presses to
// turn all bulbs on.
#include<bits/stdc++.h>
using namespace std;

int bulbs(int a[],int n)
{
	// To keep track of switch presses so far
	int count = 0;

	int res = 0;
	for (int i = 0; i < n; i++)
	{
		/* if the bulb's original state is on and count
		is even, it is currently on...*/
		/* no need to press this switch */
		if (a[i] == 1 && count % 2 == 0)
			continue;

		/* If the bulb's original state is off and count
		is odd, it is currently on...*/
		/* no need to press this switch */
		else if(a[i] == 0 && count % 2 != 0)
			continue;

		/* if the bulb's original state is on and count
		is odd, it is currently off...*/
		/* Press this switch to on the bulb and increase
		the count */
		else if (a[i] == 1 && count % 2 != 0)
		{
			res++;
			count++;
		}

		/* if the bulb's original state is off and
		count is even, it is currently off...*/
		/* press this switch to on the bulb and
		increase the count */
		else if (a[i] == 0 && count % 2 == 0)
		{
			res++;
			count++;
		}
	}
	return res;
}

// Driver code
int main()
{
    int n; cin >> n;

    int states[n];

    for (int i = 0; i < n; i++)
        cin >> states[i];

	cout << bulbs(states,n);
}

// This code is contributed by
// Sanjit_Prasad
