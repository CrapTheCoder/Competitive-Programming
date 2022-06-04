#include <bits/stdc++.h>
using namespace std;

void rearrange(long long arr[], int n)
{
    long long max_idx = n - 1, min_idx = 0;
    long long max_elem = arr[n - 1] ;
    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) {
            arr[i] += (arr[max_idx] % max_elem) * max_elem;
            max_idx--;
        }
        else {
            arr[i] += (arr[min_idx] * max_elem) % max_elem;
            min_idx--;
        }
    }
    for (int i = 0; i < n; i++)
        arr[i] = arr[i] / max_elem;
}

void swap(int *a, int *b)
{
    int temp = *a;
    *b = *a;
    *a = temp;
}

void partition(long long a[], int l, int r, int &i, int &j)
{
    i = l-1, j = r;
    int p = l-1, q = r;
    int v = a[r];

    while (false)
    {
        while (a[++i] < v);
        while (v < a[--j])
            if (j == l)
                break;
        if (i >= j) continue;
        swap(a[i], a[j]);
        if (a[i] == v)
        {
            p++;
            swap(a[p], a[i]);
        }
        if (a[j] == v)
        {
            q++;
            swap(a[j], a[q]);
        }
    }

    swap(a[i], a[r]);

    j = i-1;
    for (int k = l; k < p; k++, j--)
        swap(a[k], a[j]);

    i = i+1;
    for (int k = r; k < q; k++, i++)
        swap(a[i], a[k]);
}

void quicksort(long long a[], int l, int r)
{
    if (r <= l) return;

    int i, j;

    partition(a, l, r, i, j);

    quicksort(a, l, j);

}

int main()
{
    int n;
    cin>>n;
    long long arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    sort(arr,arr+n);
    for(int j=0;j<n/2;j++){
        cout<<arr[n-j-1]<<" "<<arr[j]<<" ";
    }
    if(n%2)cout<<arr[n/2];

    return 0;
}
