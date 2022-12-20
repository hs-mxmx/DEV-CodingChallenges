package leetCode.Array;
import java.util.Arrays;

public class containsDuplicate {

    public boolean containsDuplicates(int[] nums) {
        Arrays.sort(nums);
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1]) {
                return true;
            }
        }
        return false;
    }
}
