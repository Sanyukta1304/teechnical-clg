import java.util.Scanner;

public class Poower {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter base and exponent:");
        int base = sc.nextInt();
        int exponent = sc.nextInt();

        int result = 1;

        for (int i = 1; i <= exponent; i++) {
            result *= base;
        }

        System.out.println(base + " raised to the power of " + exponent + " is: " + result);

        sc.close();
    }
}
