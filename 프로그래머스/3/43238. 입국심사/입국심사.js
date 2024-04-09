function solution(n, times) {
    var answer = 1110;
    times.sort();
    var start = 1;
    var end = times[0]*n;
    var mid = 0;
    
    while(start <= end) {
        mid = Math.floor((start + end)/2);
        theNum = 0;
        for(var count = 0 ; count < times.length ; count++){
            theNum += Math.floor(mid/times[count]);
        }
        if(theNum < n){
            start = mid + 1;
        } else {
            //if(answer>mid)
                answer = mid;
            end = mid - 1;
        }
    }
    return answer;
}