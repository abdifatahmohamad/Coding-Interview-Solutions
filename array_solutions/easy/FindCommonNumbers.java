import java.util.ArrayList;
import java.util.List;

public class FindCommonNumbers {
    public static void main(String[] args) {
        int arr1[] = { 13, 27, 35, 40, 49, 55, 59 };
        int arr2[] = { 17, 35, 39, 40, 55, 58, 60 };
        // Output: [35, 40, 55]

        FindCommonNumbers fcn = new FindCommonNumbers();
        System.out.println(fcn.findCommonNumbers(arr1, arr2));

    }

    public List<Integer> findCommonNumbers(int[] arr1, int[] arr2) {
        List<Integer> commonNumbers = new ArrayList<Integer>();
        for (int i = 0; i < arr1.length; i++) {
            for (int j = 0; j < arr2.length; j++) {
                if (arr1[i] == arr2[j]) {
                    // Check if the list already contains the common numbers
                    if (!commonNumbers.contains(arr1[i])) {
                        // Add the common numbers into the list
                        commonNumbers.add(arr1[i]);
                    }
                }
            }
        }
        return commonNumbers;
    }
}