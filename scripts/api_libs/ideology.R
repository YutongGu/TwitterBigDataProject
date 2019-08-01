#!/usr/bin/env Rscript
# load package
library(tweetscores)
if (length(args) != 1) {
  stop("Error: screenname must be provided", call.=FALSE)
} 

args = commandArgs(trailingOnly=TRUE)
user <- args[1]
friends <- getFriends(screen_name=user, oauth="my_oauth")
results <- estimateIdeology2(user, friends)
print(results)

