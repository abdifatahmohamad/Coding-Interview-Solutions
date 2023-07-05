public class Solution
{
    public void Merge(int[] nums1, int m, int[] nums2, int n)
    {
        int last = nums1.Length - 1; // or last = m + n - 1

        // Traverse both arrays in reverse
        while (m > 0 && n > 0)
        {
            // Case 1:
            if (nums1[m - 1] > nums2[n - 1])
            {
                nums1[last] = nums1[m - 1];
                m--;
            }
            // Case 2: if nums2[n] > nums1[m] or nums2[n] > nums1[m]
            else
            {
                nums1[last] = nums2[n - 1];
                n--;
            }

            last--;
        }

        // Case 3: fill nums1 array with leftover nums2 array
        while (n > 0)
        {
            nums1[last] = nums2[n - 1];
            // Decrement both last and n pointers 
            last--;
            n--;
        }
    }
}
