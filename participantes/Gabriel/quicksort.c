//Algoritmo Quicksort.

#include <stdio.h>

// Función para intercambiar dos elementos
void cambio(float *a, float *b) {
    float c = *a;
    *a = *b;
    *b = c;
}

// Función para realizar la partición del arreglo
int particion(float v[], int mini, int maxi) 
{
    float pivote = v[maxi]; // Se usa el último elemento como pivote
    int i = (mini - 1); //último elemento más pequeño que el pivote (inicialización)

    for (int j = mini; j < maxi; j++) //j recorre el arreglo, i se queda en la posición de los elementos menores o iguales al pivote
    {
        if (v[j] <= pivote) 
        {
            i=i+1;
            cambio(&v[i], &v[j]);
        }
    }
    // Colocamos el pivote en su posición correcta
    cambio(&v[i + 1], &v[maxi]); // Intercambiamos el pivote con el elemento en la posición i+1 por si i no se ha movido
    return (i + 1); // Retorna la posición del pivote
}

// Función principal de Quicksort. Se aplica recursividad
void quicksort(float v[], int mini, int maxi)
{
    if (mini < maxi) 
    {
        // Encontramos la posición del pivote
        int pivpos = particion(v, mini, maxi);

        // Ordenamos los elementos antes y después del pivote
        quicksort(v, mini, pivpos - 1); // Llamada recursiva para la parte izquierda
        quicksort(v, pivpos + 1, maxi); // Llamada recursiva para la parte derecha
    }
}

// Función para imprimir el arreglo
void muestravec(float v[], int n) 
{
    printf("[");
    for (int i = 0; i < n; i++) {
        printf("%.2f ", v[i]); 
    }
    printf("]");
    printf("\n");
}

int main() 
{
    int n;
    printf("Ingrese el numero de elementos en el arreglo: ");
    scanf("%d", &n);

    float v[n]; 
    printf("\nIngrese los %d elementos: \n", n);
    for (int i = 0; i < n; i++) {
        printf("Elemento %d: ", i + 1);
        scanf("%f", &v[i]);
    }

    printf("\nArreglo original: \n");
    muestravec(v, n);
    quicksort(v, 0, n - 1);

    printf("\nArreglo ordenado: \n");
    muestravec(v, n);

    return 0;
}
