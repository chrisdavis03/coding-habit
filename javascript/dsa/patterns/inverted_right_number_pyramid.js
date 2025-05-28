
const invertedRightNumber = (n) => {
    for (i=n; i>0; i--){
        for (j=0; j<i; j++) {
            process.stdout.write((j+1) + "");
        }
        process.stdout.write("\n");
    }
}

invertedRightNumber(5);