function firstDuplicate(a) {
    var d = {};
    for(var i=0 ;i<=a.length; i++) {
        if (!d[a[i]])
            d[a[i]] = a[i];
        else
            return a[i];
    }
    return -1;  
}
