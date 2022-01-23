#Estructura de las funciones

promedio <- function(var1, var2, var3){
  suma <- var1 + var2 + var3
  promedio_resultado = suma / 3
  return(promedio_resultado)
}

promedio(3,4,5)#El llamado es como una función tradicional

mean(c(3,4,5))