#include <iostream>
#include <string>
using namespace std;

int main() {
    int N;
    cin >> N;
    
    string S, T;
    cin >> S >> T;
    
    string S1 = S;
    string T1 = T;
    
    for (char& c : S1) {
        if (c == 'o') {
            c = '0';
        } else if (c == 'l') {
            c = '1';
        }
    }
    
    for (char& c : T1) {
        if (c == 'o') {
            c = '0';
        } else if (c == 'l') {
            c = '1';
        }
    }
    
    if (S1 == T1) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    
    return 0;
}
