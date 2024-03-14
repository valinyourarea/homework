# homework

El código implementa un algoritmo llamado "Kadane's algorithm" que encuentra la subsecuencia continua de números con la mayor suma en una lista.

1. **Definición de la función `kadanes_algorithm(a)`**: Esta función toma una lista de números `a` como entrada y encuentra la suma máxima de una subsecuencia contigua en esa lista.

2. **Inicialización de variables**: Se inicializan algunas variables importantes:
   - `array_max` y `sum_max` comienzan con el primer número de la lista `a`.
   - `startI` y `endI` se utilizan para rastrear los índices del subarray máximo.

3. **Bucle principal**: El código recorre la lista desde el segundo elemento hasta el último.
   - `array_max` se actualiza en cada paso del bucle para seguir el rastro del subarray máximo hasta el índice actual.
   - Si `array_max` supera a `sum_max`, actualizamos `sum_max` y guardamos el índice actual como el final del subarray máximo (`endI`).

4. **Manejo de sumas negativas**: Si la suma del subarray actual se vuelve negativa, es mejor comenzar desde cero nuevamente. Por lo tanto, si `array_max` es negativo, lo reiniciamos a cero y actualizamos `startI` al siguiente índice.

5. **Impresión de resultados**: Después de salir del bucle, imprimimos el subarray máximo encontrado y su suma máxima.

~~~python
hola
~~~
