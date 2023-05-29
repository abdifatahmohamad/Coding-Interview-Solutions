public class Solution
{
    public double FindMedianSortedArrays(int[] nums1, int[] nums2)
    {
        int[] mergedArray = Merge(nums1, nums2);
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
        
        // Case 3: fill nums1 array with leftover nums1 array
        while (m > 0)
        {
            res[last] = nums1[m - 1];
            // Decrement both last and m pointers 
            last--;
            m--;
        }

        // Case 4: fill nums1 array with leftover nums2 array
        while (n > 0)
        {
            res[last] = nums2[n - 1];
            // Decrement both last and n pointers 
            last--;
            n--;
        }
        
        // List<int> ans = new List<int>();
        // foreach (int num in res)
        // {
        //     ans.Add(num);
        // }

//         string output = string.Join(", ", ans);
//         Console.WriteLine(output);
        
        
        return res;
    }
}


/*

How to find median number


int[] nums = { 1, 2, 3, 4 };
int length = nums.Length;
int median;

if (length % 2 == 0)
{
    // Even length: average of the two middle elements
    int index1 = length / 2;
    int index2 = (length / 2) - 1;
    median = (nums[index1] + nums[index2]) / 2;
}
else
{
    // Odd length: middle element
    int index = (length - 1) / 2;
    median = nums[index];
}

Console.WriteLine("Median: " + median);


*/
