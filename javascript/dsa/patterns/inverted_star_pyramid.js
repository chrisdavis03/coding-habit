
const invertedStarPyramid = (n) => {


    for (i=n; i>0; i--) {
        //prepended space characters
        for (j=0; j<(n-i); j++) {
            process.stdout.write(' ');
        };
        //asterisk characters
        for (j=0; j<(i*2)-1; j++){
            process.stdout.write('*');
        };
        //trailing spaces
        for (j=0; j<(n-i); j++) {
            process.stdout.write(' ');
        };
        process.stdout.write("\n");
    };
}

invertedStarPyramid(6);