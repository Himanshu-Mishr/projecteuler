#include <stdio.h>

int main() {
    long long int n, a, b, k, count = 0;
    scanf("%lld", &n);
    for (long long int i = 0; i < n; ++i)
    {
        count = 0;
        scanf("%lld %lld %lld", &a, &b, &k);
        for (long long int j = 0; j < a; ++j)
        {
            for (long long int p = 0; p < b; ++p)
            {
                if ((j&p) < k) {
                    count++;
                }
            }
        }
    printf("Case #%lld: %lld\n", i+1, count);
    }
    return 0;
}
