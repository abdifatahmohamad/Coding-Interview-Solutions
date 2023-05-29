public class Solution
{
    public double FindMedianSortedArrays(int[] nums1, int[] nums2)
    {
        int[] mergedArray = Merge(nums1, nums2);
        
        // foreach(int n in mergedArray){
        //     Console.WriteLine(n);
        // }
        
        int count = mergedArray.Length;

        if (count % 2 == 0)
        {
            int midIndex = count / 2;
            return (mergedArray[midIndex - 1] + mergedArray[midIndex]) / 2.0;
        }
        else
        {
            int midIndex = count / 2;
            return mergedArray[midIndex];
        }
    }

    private static int[] Merge(int[] nums1, int[] nums2)
    {
        int m = nums1.Length;
        int n = nums2.Length;
        int[] res = new int[m + n];
        //int last = nums1.Length - 1; // or last = m + n - 1
        int last = m + n - 1;

        // Traverse both arrays in reverse
        while (m > 0 && n > 0)
        {
            // Case 1:
            if (nums1[m - 1] > nums2[n - 1])
            {
                res[last] = nums1[m - 1];
                m--;
            }
            // Case 2: if nums2[n] > nums1[m] or nums2[n] > nums1[m]
            else
            {
                res[last] = nums2[n - 1];
                n--;
            }

            last--;
        }

        // Case 3: fill nums1 array with leftover nums2 array
        while (n > 0)
        {
            res[last] = nums2[n - 1];
            // Decrement both last and n pointers 
            last--;
            n--;
        }
    
        for (int i = 0; i < res.Length; i++){
            Console.WriteLine($"Index: {i} Number: {res[i]}");
        }
        
        // Case 4: fill nums1 array with leftover nums1 array
        while (m > 0)
        {
            res[last] = nums1[m - 1];
            // Decrement both last and m pointers 
            last--;
            m--;
        }
        
        
        return res;
    }
}
