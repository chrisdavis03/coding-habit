//Right-Angled Triangle Pattern

const rightTri = (n) => {
    for (i=0; i<n; i++){
    
        for (j=0; j<=i; j++){
            process.stdout.write('* ');
        };
        process.stdout.write('\n');
    };
};

rightTri(5);