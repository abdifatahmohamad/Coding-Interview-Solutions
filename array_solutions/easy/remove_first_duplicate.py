'''

https://app.codesignal.com/interview-practice/task/pMvymcahZ8dY4g75q/description


Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return -1.

Example

For a = [2, 1, 3, 5, 3, 2], the output should be solution(a) = 3.

There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a smaller index than the second occurrence of 2 does, so the answer is 3.

For a = [2, 2], the output should be solution(a) = 2;

For a = [2, 4, 3, 5, 1], the output should be solution(a) = -1.

'''
# Using bucket


def solution(a):
    max_val = max(a)
    bucket = [0 for _ in range(max_val + 1)]
    for n in a:
        if bucket[n] > 0:
            return n
        bucket[n] += 1

    return -1

# using set:


def solution(a):
    arraySet = set()
    for n in a:
        if n in arraySet:
            return n
        arraySet.add(n)
    return -1


# Java
int solution2(int[] a) {
    int[] bucket = new int[a.length + 1];
    for (int n: a){
        if (bucket[n] > 0){
            return n; }
        bucket[n] + +;}

    return -1;}


print(solution([5, 6, 7, 8, 7]))
