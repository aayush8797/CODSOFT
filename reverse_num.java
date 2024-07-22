public class reverse_num{

    public static void reverse(int num[]){

        int first =0;
        int last = num.length-1;

        while(first<last){

            int temp=num[first];
            num[first]=num[last];
            num[last]=temp;

            first++;
            last--;
        }
    }

    public static void main(String[] args) {
        
        int num[] = {34,87,90,65,76,45,23};
        reverse(num);
        System.out.print("The reverse number is : ");
        for(int i=0; i<num.length;i++){
            System.out.print(num[i]+" ");
        }
    }
}