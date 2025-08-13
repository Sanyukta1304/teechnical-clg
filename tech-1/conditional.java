import java.util.Scanner;

public class conditional {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter two number:");
        int a = sc.nextInt();
        int b = sc.nextInt();
       
        if (a<b) {
            System.out.println( "b is great than a");
        }else if (a>b) {
            System.out.println("a is great than b");
        }else {
            System.out.println("b is euqal a");
        }
    }
}
    
    

