function bubble_sort(arr){
    let isSwap;
    do {
    isSwap = false;
    for(let i=0;i<arr.length;i++){
        if(arr[i]>arr[i+1]){
            let temp = arr[i];
            arr[i] = arr[i+1];
            arr[i+1] = temp;
            isSwap = true;
        }
    }
    return arr;
}