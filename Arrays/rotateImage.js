function rotateImage(a) {
    a.reverse();
    for(let i=0;i<a.length;i++){
        for(let j=0;j<i;j++){
            let temp = a[i][j];
            a[i][j] = a[j][i];
            a[j][i] = temp;
        }  
    }
    return a
}
