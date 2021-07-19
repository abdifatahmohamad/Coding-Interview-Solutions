import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;

public class FindCommonNumbers {
    public static void main(String[] args) {
        int arr1[] = { 13, 27, 35, 40, 49, 55, 59 };
        int arr2[] = { 17, 35, 39, 40, 55, 58, 60 };
        // Output: [35, 40, 55]

        System.out.println(findCommonNumbers(arr1, arr2));
    }

    // Brute force approach
    public static List<Integer> findCommonNumbers(int[] arr1, int[] arr2) {
        List<Integer> result = new ArrayList<Integer>();
        for (int i = 0; i < arr1.length; i++) {
            for (int j = 0; j < arr2.length; j++) {
                if (arr1[i] == arr2[j])
                    result.add(arr1[i]);
            }
        }
        return result;
    }

    // HashMap O(N) Time || O(N) Space
    public static List<Integer> findCommonNumbers(int[] arr1, int[] arr2) {

        HashMap<Integer, Integer> map = new HashMap();
        List<Integer> newList = new ArrayList<Integer>();

        for (int num : arr1) {
            /**
             * if(map.containsKey(num)){ map.put(num, map.get(num) + 1); }else{ map.put(num,
             * 1); }
             */

            // Same as above code but shorter way:
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        for (int el : arr2) {
            if (map.containsKey(el)) {
                newList.add(el);
            }
        }
        return newList;
    }
}