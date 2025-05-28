
const invertedRight = (n) => {
    for (i=n; i>0; i--){
        for (j=i; j>0; j--) {
            process.stdout.write('*');
        }
        process.stdout.write("\n");
    }
}

invertedRight(5);