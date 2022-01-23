#### Rutas de ejemplo
#UBICACION DE DIRECTORIO PARA LECTURA DE DATOS
setwd("C:/Users/erika/OneDrive/Desktop/Clases-Eafit/Introduccion-a-la-programacion/Clase 14/practica1/datos")
#CODIGO DEL PROYECTO
setwd("C:/Users/erika/OneDrive/Desktop/Clases-Eafit/Introduccion-a-la-programacion/Clase 14/practica1")
#EXPORTAR RESULTADOS O MOSTRARLOS
setwd("C:/Users/erika/OneDrive/Desktop/Clases-Eafit/Introduccion-a-la-programacion/Clase 14/practica1/resultados")

#Variables en R
x <- 56
y <- "Hola mundo"
z <- x>10
a <- 45.7

#Datos de tipo vector
materias <- c('Biología', 'Matemáticas', 'Química')

########### Para manipular y acceder a elementos de un vector ########################
materias[2] #Seleccion por posición
materias[c(1,3)] #Seleccion por vector


#####################################################################################


#Datos de tipo Lista
numeros <- c(1,2,3,4,5,6,7,8,9,10) #Vector
numeros_automaticos <- (1:100) #Vector
lista_variables <- c(x,y,z)

nombre_materias <- c("Biología", "Matemáticas", "Química")
notas_materias <- matrix(c(4.3,4.2,4.1, 3.9, 2.3, 4.5, 4.1, 3.8, 2.0), nrow=3, ncol=3)

lista_final <- list(nombre_materias, notas_materias)
names(lista_final) <- c('vector', 'matriz')
lista_final[['vector']][2]
lista_final[['matriz']][3,2]
#Agregar un elemento nuevo a la lista
#lista_final[['otro']] <- objeto

########### Para manipular y operar datos de tipo Lista ########################
###############################################################################


#Datos de tipo matrix
m <- matrix( c('x', 'y', 'z', 'a', 'b', 'c'), nrow=2, ncol=3, byrow=TRUE)
m2 <- matrix( c('x', 'y', 'z', 'a', 'b', 'c'), nrow=2, ncol=3, byrow=FALSE)
mn <- matrix( c(10,20,03,15,12,20,08,19,18,19), nrow=5, ncol=2)
#colname para agregar nombre a la columna, y rowname para el nombre de la fila
colnames(mn) <- c('año1', 'año2')

disney <- c(11,13,11,8,12)
warner <- c(20,20,16,17,22)

peliculas <- matrix(c(warner,disney), nrow=5, ncol=2)
colnames(peliculas) <- c('warner', 'disney')
rownames(peliculas) <- c('2017','2018', '2019', '2020', '2021')


########### Para manipular, acceder y operar (operaciones básicas) con los objetos de una matriz ########################
mn + mn #suma de matrices
mn * mn #multiplicación de matrices
# Las multiplicaciones en R son elemento a elemento, no ocurren como el algebra lineal
# Para multiplicar matrices como el algebra lineal %*%

########################################################################################

#Datos de tipo arreglo
a <- array(c('perros', 'gatos'), dim = c(3,4,2))
########### Para manipular y acceder a los objetos de una matriz ########################
peliculas[4,2] #Obtener un solo elemento
peliculas['2020', 'warner'] #Obtener un solo elemento por nombre
peliculas [c(3,2), c(2,1)] #Obtener elementos agrupados
peliculas [c(3,2), c('warner','disney')] #Obtener elementos por vector y nombre
peliculas[5,] #Obtener por fila o reglón
peliculas['2021',] #Obtener por fila o reglón


########################################################################################


#Datos de tipo dataframe

df1 <- iris
iris_sepalo <- iris$Petal.Width

########### Para manipular y acceder a los objetos de un dataframe ########################
df1[,2] #Para obtener columna
df1[,'Species'] #Obtener columna por nombre
df1$Species #Obtener columna por simbolo

df1[1,] #Para obtener renglón o fila

df1[3,2] #Obtener solo un elemento

df1[3,'Sepal.Length'] #Seleccionar un elemento del dataframe usando nombre de la columna

df1[c(3,4), c(2,3)] #Seleccionar más de un elemento del dataframe
df1[c(3,4), c('Sepal.Length', 'Species')] #Seleccionar más de un elemento del dataframe por nombre


#Ordenar dataframe

indices <- order(df1$Petal.Width, decreasing = FALSE) #De menor a mayor
indices2 <- order(df1$Petal.Width, decreasing = TRUE) #De mayor a menor
df1[indices,]
df1[indices2,]
names(df1) <- c("S.Length", "S.Width", "P.Length", "P.Width", "Especies")

##########################################################################################

#Factores

calificaciones <- c(4.2,3.0,3.0,4.5,2.0,2.0,2.1,3.0,3.0,4.5)
calificaciones_factor <- factor(calificaciones)
#Levels, labels
#ordered = TRUE
plot(calificaciones_factor)

