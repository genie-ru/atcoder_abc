#include <bits/stdc++.h>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int H, W;
  cin >> H >> W;
  vector<string> A(H), B(H);
  for (string& x : A) cin >> x;
  for (string& x : B) cin >> x;
  bool match = false;
  for (int s = 0; s < H && !match; s++) {
    for (int t = 0; t < W && !match; t++) {
      bool ok = true;
      for (int i = 0; i < H && ok; i++) {
        for (int j = 0; j < W && ok; j++) {
          if (A[(i - s + H) % H][(j - t + W) % W] != B[i][j]) ok = false;
        }
      }
      if (ok) {
        cout << "Yes\n";
        match = true;
      }
    }
  }
  if (!match) cout << "No\n";
  return 0;
}
