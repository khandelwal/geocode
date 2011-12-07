communities <- read.csv('zipcode_weighted.txt', header=F, sep=",")
head(communities)
library(zipcode)
data(zipcode)
communities$zip = clean.zipcodes(communities$V1)
mergeddata = merge(communities, zipcode, by.x='zip', by.y='zip')


library(ggplot2)
g = ggplot(data=mergeddata) + geom_point(aes(x=longitude, y=latitude, colour=V2)) 
g = g + theme_bw() + scale_x_continuous(limits = c(-125, -66), breaks = NA)
g = g + labs(x=NULL, y=NULL)
ggsave(g, width=6, height=4, filename="zips.png")






