#define MAX(A,B)(A>B?A:B)
int findMaxConsecutiveOnes(int* nums, int numsSize){
    int maxres=0;
    int i=0;
    while(i<numsSize)
    {
        int countones=0;
        while(i<numsSize && nums[i]==1)
        {
            countones++;
            i++;  
        }
        maxres=MAX(maxres,countones);
        i++;
    }
    return maxres;
}
