input = matrix(c(1,1,0,
		1,0,1,
		0,1,1,
		0,0,1),3,4)
w = matrix(runif(3)-0.5,1,3)
target = matrix(c(1,1,1,0),1,4)
eta = 0.2

for( i in 1:10 ){
	H = w%*%input
	output = ifelse(H>0,1,0)
	recentw = eta*(target-output)%*%t(input)
	w = recentw - w
	prmatrix(w)
}

plot(matrix(w))
