library(ISLR)
model = lm(mpg ~ . - name, data=Auto)
par(mfrow=c(2,2))
plot(model)