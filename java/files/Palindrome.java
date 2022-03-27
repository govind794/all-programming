// public class Palindrome{

//     public static void main(String[] args){
//         int r, result, sum=0;
//         int n = 4942;

//         result = n;
        
//         while(n>0){
//             r=n%10;
//             sum = (sum*10)+r;
//             n= n/10;
//         }

//         if(result == sum){
//             System.out.println("Palindrome number");
//         }else{
//             System.out.println("Not Palindrome");
//         }
//     }
// }

public class Palindrome{

    public static boolean isPalindrome(String str){
        int i=0, j= str.length() - 1;
        int n = 494;
        
        while(i < j){
            if(str.charAt(i) != str.charAt(j))
                return false;
            
            i++;
            j--;
        }

        return true;
    }


    public static void main(String[] args){
        String str = "gaagw";

        if(isPalindrome(str)){
            System.out.println("Yes");
        }else{
            System.out.println("No");
        }
    }
}
