import java.util.ArrayList;
import java.util.Scanner;
import java.util.TreeSet;

public class Main {

	public static void main(String[] args) {
		// TODO 自動生成されたメソッド・スタブ
		Scanner sc = new Scanner(System.in);
		long n = sc.nextLong();
		int ans = 0;
		int max = 300000;
		TreeSet<Integer> set = new TreeSet<>();
		ArrayList<Integer> prime = new ArrayList<>();
		for (int i = 2; i < max; i++) {
			set.add(i);
		}
		while (!set.isEmpty()) {
			int t = set.first();
			prime.add(t);
			int i = 1;
			while (t * i <= max) {
				set.remove(t * i);
				i++;
			}
		}

		int a, b, c;
		int now = 0;
		a = prime.get(now);
		while (Math.pow(a, 5) < n) {
			a = prime.get(now);
			b = prime.get(now + 1);
			c = prime.get(now + 2);
			for (int i = now + 1; (long)a * a * b * c * c <= n; i++) {
				b = prime.get(i);
				c = prime.get(i + 1);
				int t = (int) Math.sqrt(n / (double) (a * a * b));
				for (int j = i + 1; prime.get(j) <= t; j++) {
					ans++;
				}
			}
			now++;
		}

		System.out.println(ans);
	}
}