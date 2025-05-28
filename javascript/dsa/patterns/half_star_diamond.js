
//process.stdout.write(' ');

const halfStarDiamond = (n) => {
    // n 1 rows, n columns max

    for (i=1; i<=(n*2); i++) {
        //write columns
        //increment
        if (i <=n ) {
            for (j=1; j<=i; j++) {
                process.stdout.write('*');
            };
        } else {
            //decrement
            for (j=(2 * n - i); j>0; j--) {
                process.stdout.write('*');
            };
    }''
        process.stdout.write('\n');
    };
}

halfStarDiamond(5);