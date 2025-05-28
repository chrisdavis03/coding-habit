
//process.stdout.write(' ');

const starDiamond = (n) => {
    //star pyramid
    for (i=1; i<=n; i++){
        //leading spaces
        for (j=n; j>i; j--) {
            process.stdout.write(" ") 
        };
        //stars
        for (j=0; j<(2 * i)-1; j++) { 
            process.stdout.write("*")
        };
        //trailing spaces
        for (j=(n-i); j>0; j--) { 
            process.stdout.write(" ")
        };
        process.stdout.write("\n")
    };
    //inverted star pyramid
        for (i=n; i>=1; i--){
        //leading spaces
        for (j=n; j>i; j--) {
            process.stdout.write(" ") 
        };
        //stars
        for (j=0; j<(2 * i)-1; j++) { 
            process.stdout.write("*")
        };
        //trailing spaces
        for (j=(n-i); j>0; j--) { 
            process.stdout.write(" ")
        };
        process.stdout.write("\n")
    };
}

starDiamond(5);