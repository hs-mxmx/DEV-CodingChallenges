package leetCode.Array;
import java.util.Arrays;

public class intersectionTwoArrays {

    public int[] intersect(int[] nums1, int[] nums2) {
        int size = nums1.length < nums2.length ? nums1.length : nums2.length;
        int[] temp = new int[size];
        int fixedPosition = 0;
        int resultPosition = 0;

        // Sort arrays
        Arrays.sort(nums1);
        Arrays.sort(nums2);

        // Iterate through first array
        for(int i = 0; i < nums1.length; i++){
            // Iterate thorugh second array
            for(int j = fixedPosition; j < nums2.length; j++){
                // (3,3,5,6) | (1,2,3)
                // Case where first iterated element is bigger than second one (Fixing position for second array)
                if (nums1[i] > nums2[j]) {
                    fixedPosition++;
                // Default case
                } else if(nums1[i] == nums2[j]){
                    temp[resultPosition] = nums1[i];
                    fixedPosition++;
                    resultPosition++;
                    break;
                }
            }
        }

        int[] result = new int[resultPosition];
        for(int x = 0; x < resultPosition; x++){
            result[x] = temp[x];
        }
        return result;
    }

}