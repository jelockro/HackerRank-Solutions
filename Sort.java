import java.io.*;
import java.util.*;

public class Sort {

  public static void insertionSortPart2(int[] ar){       
         // Fill up the code for the required logic here
         // Manipulate the array as required
         // The code for Input/Output is already provided

    int length = ar.length;
    for (int i = 1; i < length; i++){
       int x = ar[i];
       int j = i;
       //System.out.println("x = " + x + "; j = " + j);
       
       //if (ar[j-1] > x){System.out.print("Should be in loop");}
      
       while ((j > 0) && (ar[j-1] > x)){
           //System.out.println("entered loop");
           
           ar[j] = ar[j-1];
           j--;
           
          //print loop
          /* for (int k = 0; k < length; k++){
               System.out.print(ar[k]+ " ");
           }
           System.out.println();*/
           
       }
       //System.out.print("j is:" + j + "& i is:" + i) ;
       
       ar[j] = x;
       
       if (j != i){     
           for (int k = 0; k < length; k++){
               System.out.print(ar[k]+ " ");
           }
           System.out.println();
       } 
  
    } //for loop

  }
    
 
    
    
    
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int s = in.nextInt();
    int[] ar = new int[s];
    
    for(int i=0;i<s;i++){
      ar[i]=in.nextInt(); 
     }
    insertionSortPart2(ar);    
                  
  }  

  private static void printArray(int[] ar) {
    
    for(int n: ar){
       System.out.print(n+" ");
    }
    
    System.out.println("");
 }
}
