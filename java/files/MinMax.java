public class MinMax{

    public static void main(String[] args){
        int inArray[] = {2,90,3,72,6,1,7,8,34,76,22,98};
		int arraySize = inArray.length;
		findMinMax(inArray, arraySize); 
    }

   private static void findMinMax(int[] inArray, int arraySize){
        int min = inArray[0];
        int indexMin = 0;
        int max = inArray[0];
        int indexMax = 0;

        for(int i=0; i<arraySize; i++){
            if(inArray[i] > max){
                max = inArray[i];
                indexMax = i;
            }

            if(inArray[i] < min){
                min = inArray[i];
                indexMin = i;
            }
        }

        System.out.println("Min= " + min);
        System.out.println("Max= " + max);

        System.out.println("IndexMin= " + indexMin);
        System.out.println("IndexMax= " + indexMax);
   }
}