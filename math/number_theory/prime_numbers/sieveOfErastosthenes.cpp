#include<bits/stdc++.h>

using namespace std;

vector<int> sieveOfErastosthenes(int limit){
    vector<int> primes;
    vector<bool> isPrime(10e5);
    fill(isPrime.begin(), isPrime.end(), true);

    for (int i = 2; i <= limit; i++) {
        if (isPrime[i]) {
            for (int j = i * i; j <= limit; j += i) {
                isPrime[j] = false;
            }
            primes.push_back(i);
        }
    }
    return primes;
}
