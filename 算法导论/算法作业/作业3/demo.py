#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

typedef long long LL;

const int maxn = 1e6 + 10;

int a[maxn];
set<LL> se;

void calculateSubarraySums(int left, int right) {
    if (left > right) {
        return;
    }

    LL sum = 0;
    for (int i = left; i <= right; i++) {
        sum += a[i];
    }
    se.insert(sum);

    int mid = upper_bound(a + left, a + right + 1, (a[left] + a[right]) / 2) - a;

    if (mid == right + 1) {
        return;
    }

    if (mid - 1 >= left) {
        calculateSubarraySums(left, mid - 1);
    }
    if (mid <= right) {
        calculateSubarraySums(mid, right);
    }
}

int main() {
    int T;
    cin >> T;

    while (T--) {
        int n, q;
        cin >> n >> q;

        for (int i = 1; i <= n; i++) {
            cin >> a[i];
        }

        sort(a + 1, a + n + 1);

        se.clear();

        calculateSubarraySums(1, n);

        for (int i = 1; i <= q; i++) {
            LL x;
            cin >> x;
            if (se.count(x)) {
                cout << "Yes" << endl;
            }
            else {
                cout << "No" << endl;
            }
        }
    }

    return 0;
}