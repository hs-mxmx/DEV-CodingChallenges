package leetCode.Array;
import java.util.Arrays;

public class singleNumber {
    
    public int singleNumbers(int[] nums) {
        Arrays.sort(nums);
        int result = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (i == nums.length - 1 && nums[i] != nums[i - 1]) {
                result = nums[i];
            } else if (nums[i] != nums[i - 1] && nums[i] != nums[i + 1]) {
                result = nums[i];
            }
        }
        return result;
    }
}
