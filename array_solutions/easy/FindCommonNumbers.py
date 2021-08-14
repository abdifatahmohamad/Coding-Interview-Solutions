from typing import List


# Brute force approach Solution O(N^2) Time || O(N) Space
def findCommonNumbers(arr1: List, arr2: List) -> List:
    res = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                res.append(arr1[i])
    return res


# Hash Map Solution O(N) Time || O(N) Space
def findCommonNumbers(arr1: List, arr2: List) -> List:
    mapping = {}
    res = []
    for num in arr1:
        mapping[num] = mapping.get(num, 0) + 1

    for el in arr2:
        if el in mapping:
            res.append(el)
    return res


arr1 = [13, 27, 35, 40, 49, 55, 59]
arr2 = [17, 35, 39, 40, 55, 58, 60]
print(findCommonNumbers(arr1, arr2))  # Output: [35, 40, 55]

# Java Solution:
# import java.util.ArrayList;
# import java.util.List;
# import java.util.HashMap;

# public class FindCommonNumbers {
#     public static void main(String[] args) {
#         int arr1[] = { 13, 27, 35, 40, 49, 55, 59 };
#         int arr2[] = { 17, 35, 39, 40, 55, 58, 60 };
#         // Output: [35, 40, 55]

#         System.out.println(findCommonNumbers1(arr1, arr2));
#         System.out.println(findCommonNumbers2(arr1, arr2));
#     }

#     // Brute force approach
#     public static List<Integer> findCommonNumbers1(int[] arr1, int[] arr2) {
#         List<Integer> result = new ArrayList<Integer>();
#         for (int i = 0; i < arr1.length; i++) {
#             for (int j = 0; j < arr2.length; j++) {
#                 if (arr1[i] == arr2[j])
#                     result.add(arr1[i]);
#             }
#         }
#         return result;
#     }

#     // HashMap O(N) Time || O(N) Space
#     public static List<Integer> findCommonNumbers2(int[] arr1, int[] arr2) {

#         HashMap<Integer, Integer> map = new HashMap();
#         List<Integer> newList = new ArrayList<Integer>();

#         for (int num : arr1) {
#             /**
#              * if(map.containsKey(num)){ map.put(num, map.get(num) + 1); }else{ map.put(num,
#              * 1); }
#              */

#             // Same as above code but shorter way:
#             map.put(num, map.getOrDefault(num, 0) + 1);
#         }

#         for (int el : arr2) {
#             if (map.containsKey(el)) {
#                 newList.add(el);
#             }
#         }
#         return newList;
#     }
# }
