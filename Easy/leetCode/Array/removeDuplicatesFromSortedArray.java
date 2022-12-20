package leetCode.Array;
import java.util.Arrays;

public class removeDuplicatesFromSortedArray {

    public int removeDuplicates(int[] nums) {
        // If sorted
        return removeDuplicatesSorted(nums);
    }
    public int removeDuplicatesSorted(int[] nums) {
        // {0,0,1,2,2,3,4,5,5,5,6,7,9,10};
        int[] result = new int[nums.length];
        int n = 0;
        boolean duplicated = false;

        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == nums[i + 1]) {
                duplicated = true;
            } else if (nums[i] != nums[i + 1] && !duplicated) {
                result[n] = nums[i];
                n++;
            } else if (nums[i] != nums[i + 1]) {
                duplicated = false;
            }
        }

        if (!duplicated) {
            result[n] = nums[nums.length - 1];
            n++;
        }

        System.out.println(Arrays.toString(result));
        return n;
    }
}
