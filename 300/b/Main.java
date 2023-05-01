import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int H = scanner.nextInt();
        int W = scanner.nextInt();
        String[] A = new String[H];
        String[] B = new String[H];
        for (int i = 0; i < H; i++) {
            A[i] = scanner.next();
        }
        for (int i = 0; i < H; i++) {
            B[i] = scanner.next();
        }
        boolean match = false;
        for (int s = 0; s < H && !match; s++) {
            for (int t = 0; t < W && !match; t++) {
                boolean ok = true;
                for (int i = 0; i < H && ok; i++) {
                    for (int j = 0; j < W && ok; j++) {
                        if (A[(i - s + H) % H].charAt((j - t + W) % W) != B[i].charAt(j)) {
                            ok = false;
                        }
                    }
                }
                if (ok) {
                    System.out.println("Yes");
                    match = true;
                }
            }
        }
        if (!match) {
            System.out.println("No");
        }
    }
}
