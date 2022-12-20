package leetCode.Array;
public class Main {
    public static void main(String[] args) {
        intersectionTwoArrays hello = new intersectionTwoArrays();
        /*
        int[] nums = {0,0,1,2,2,3,4,5,5,5,6,7,9,10};
        int n = hello.removeDuplicates(nums);
        
        int nums[] = {7,1,5,3,6,4};
        int n = hello.maxProfit(nums);

        int nums[] = {7,1,5,3,6,4};
        hello.rotate(nums, 3);
        */

        int[] nums1 = {4,9,5};
        int[] nums2 = {9,4,9,8,4};
        //int total = hello.singleNumber(nums);

        int[] intersectResult = hello.intersect(nums1, nums2);

        // System.out.println(n);
    }
}
