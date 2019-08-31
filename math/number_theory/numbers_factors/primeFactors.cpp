#include<bits/stdc++.h>

using namespace std;

// TODO: Make files as modules and import them
vector<int> sieveOfErastosthenes(int limit){
    vector<int> primes;
    vector<bool> isPrime(10e5);
    fill(isPrime.begin(), isPrime.end(), true);
    for(int i = 2; i <= limit; i++){
        if(isPrime[i]){
            for(int j = 2*i; j <= limit; j += i) {
                isPrime[j] = false;
            }
            primes.push_back(i);
        }
    }
    return primes;
}

vector<int> primeFactors(int number){
    vector<int> factors;
    vector<int> primes = sieveOfErastosthenes(number);
    int primeFactorIndex = 0, primeFactor = primes[primeFactorIndex];

    while(primeFactor * primeFactor <= number){
        while(number % primeFactor == 0){
            number /= primeFactor;
            factors.push_back(primeFactor);
        }
        primeFactor = primes[++primeFactorIndex];
    }

    if(number != 1)
        factors.push_back(number);
    return factors;
}

