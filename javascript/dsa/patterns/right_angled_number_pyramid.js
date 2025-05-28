//Right-Angled Number Pyramid Pattern

const rightPyramid = (n) => {
    for (i=0; i<n; i++){
    
        for (j=0; j<=i; j++){
            process.stdout.write((j+1) + ' ');
        };
        process.stdout.write('\n');
    };
};

rightPyramid(5);