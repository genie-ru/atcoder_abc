#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    
    vector<vector<int>> a(M, vector<int>(N));
    
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            cin >> a[i][j];
        }
    }
    
    int ans = 0;
    
    for (int i = 1; i <= N; i++) {
        for (int j = i + 1; j <= N; j++) {
            bool flag = false;
            
            for (int k = 0; k < M; k++) {
                for (int l = 0; l < N - 1; l++) {
                    if ((a[k][l] == i && a[k][l + 1] == j) || (a[k][l] == j && a[k][l + 1] == i)) {
                        flag = true;
                        break;
                    }
                }
                if (flag) {
                    break;
                }
            }
            
            if (!flag) {
                ans++;
            }
        }
    }
    
    cout << ans << endl;
    
    return 0;
}
