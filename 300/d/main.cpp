#include <iostream>
#include <string>
#include <vector>
using namespace std;

const long long Z = 1000000;
bool isprime[Z+1] = {};
int count_primes[Z+1] = {};
vector<long long> primes;


int main(){
    for(int p=2; p<=Z; p++) isprime[p] = true;
    for(int p=2; p*p<=Z; p++) if(isprime[p]){
        for(int q=p*p; q<=Z; q+=p) isprime[q] = false;
    }
    for(int p=2; p<=Z; p++) if(isprime[p]){
        primes.push_back(p);
        count_primes[p] = 1;
    }
    for(int p=2; p<=Z; p++) count_primes[p] += count_primes[p-1];

    long long N; cin >> N;
    long long ans = 0;
    for(long long a=2; a*a*a*a*a<=N; a++) if(isprime[a]) {
        for(long long c=a+1; a*a*a*c*c<=N; c++) if(isprime[c]) {
            long long br = min(c-1, N/(a*a*c*c));
            long long bl = a;
            if(bl < br) {
                ans += count_primes[br];
                ans -= count_primes[bl];
            }
        }
    }
    cout << ans << endl;
    return 0;
}
