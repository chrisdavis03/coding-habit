
const starPyramid = (n) => {
    for (i=1; i<=n; i++){
        // process.stdout.write(i + "")
        // process.stdout.write("\t")
        for (j=n; j>i; j--) {
            process.stdout.write(' ');
        }
        process.stdout.write("*".repeat((i*2)-1) + "\n");
    }
}

starPyramid(6);