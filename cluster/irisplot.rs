data = read.csv(file="./result/result.csv", header=FALSE, sep=",")
x = (1:dim(data)[2])
size = dim(data)[1]/2

jpeg("iris_random_assign.jpeg")
color = rainbow(size)
plot(0,0,xlab="iterator",ylab="sse",xlim=c(1,max(x)),ylim=c(min(data),max(data)),type="n")
for ( i in 1:size ){
	lines(x, data[i,], col=color[i],  type="l")
}
dev.off()

jpeg("iris_with_definer.jpeg")
color = rainbow(size)
plot(0,0,xlab="iterator",ylab="sse",xlim=c(1,max(x)),ylim=c(min(data),max(data)),type="n")
for ( i in size+1:dim(data)[1] ){
	lines(x, data[i,], col=color[i-size], type="l")
}
dev.off()
