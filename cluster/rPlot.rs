data = read.csv(file="./result/sse.csv", header=FALSE, sep=",")
x = (1:dim(data)[2])
size = dim(data)[1]/3

jpeg("assign_random.jpeg")
color = rainbow(size)
plot(0,0,xlab="iterator",ylab="sse",xlim=c(1,max(x)),ylim=c(min(data),max(data)),type="n")
for ( i in 1:size ){
	lines(x, data[i,], col=color[i],  type="l")
}
dev.off()

jpeg("assign_definer.jpeg")
color = rainbow(size)
plot(0,0,xlab="iterator",ylab="sse",xlim=c(1,max(x)),ylim=c(min(data),max(data)),type="n")
for ( i in size+1:dim(data)[1] ){
	lines(x, data[i,], col=color[i-size], type="l")
}
dev.off()

jpeg("assign_bad_definer.jpeg")
color = rainbow(size)
plot(0,0,xlab="iterator",ylab="sse",xlim=c(1,max(x)),ylim=c(min(data),max(data)),type="n")
for ( i in (size*2)+1:dim(data)[1] ){
	lines(x, data[i,], col=color[i-(size*2)], type="l")
}
dev.off()

jpeg("assign_random_zoom.jpeg")
color = rainbow(size)
plot(0,0,xlab="iterator",ylab="sse",xlim=c(1,10),ylim=c(50,200),type="n")
for ( i in 1:size ){
	lines(x, data[i,], col=color[i],  type="l")
}
dev.off()

jpeg("assign_definer_zoom.jpeg")
color = rainbow(size)
plot(0,0,xlab="iterator",ylab="sse",xlim=c(1,10),ylim=c(50,200),type="n")
for ( i in size+1:dim(data)[1] ){
	lines(x, data[i,], col=color[i-size], type="l")
}
dev.off()

jpeg("assign_bad_definer_zoom.jpeg")
color = rainbow(size)
plot(0,0,xlab="iterator",ylab="sse",xlim=c(1,10),ylim=c(50,200),type="n")
for ( i in (size*2)+1:dim(data)[1] ){
	lines(x, data[i,], col=color[i-(size*2)], type="l")
}
dev.off()

