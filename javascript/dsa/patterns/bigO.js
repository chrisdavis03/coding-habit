
const n=5
let count = 0

for (i=0; i<n; i++){
	let o  = []
	count+=1;
	for (j=0; j<=i; j++){
		o.push(j)
		count += 1;
	};
	console.log("i=" + i + "j=" + o);
};

console.log(count);