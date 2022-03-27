public class SortOrNot{

    public static void main(String[] args){
        int[] inArray = {1,5,4,7,8,2};
        // int[] inArray = {1,5,6,8,9};
        int arraySize = inArray.length;
        System.out.println(isSorted(inArray,arraySize));
    }

    public static boolean isSorted(int[] inArray, int arraySize){
        for(int i=0; i<arraySize-1; i++){
            if(inArray[i] > inArray[i+1]){
                return false;
            }
        }

        return true;
        }
}