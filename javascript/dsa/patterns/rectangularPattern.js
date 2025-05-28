const rectangularPattern1 = (n) => {
    row=[]
    col=[]
    for (i=0; i<n; i++){
        col.push('*');
    };

    for (i=0; i<n; i++){
        row.push(col);
    };
    return row;
};
const rectangularPattern2 = (n) => {
    for (i=0; i<n; i++){
        process.stdout.write('* ');
        for (j=0; j<(n-1); j++){
            process.stdout.write('* ');
         };
         process.stdout.write('\n')
    };
};

// rectangularPattern1(8);
rectangularPattern2(5)