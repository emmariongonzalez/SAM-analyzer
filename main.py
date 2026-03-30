# Script by Emma Rion Gonzalez for the microcredential "basic digital competences for computational biology"
# To run the script use: python3 main.py ~/dia9/nf/2-Align/WT.sam
import sys

# Define the path as input
def main():
    # Look how many arguments form the entry command, there shoiuld be only 2 maximum
    if len(sys.argv) < 2:
        print("Uso: python3 main.py <ruta_al_archivo>")
        sys.exit(1)
    # Use the second argument as input for fichero_sam 
    fichero_sam = sys.argv[1]

    # Start the counter of reads alineations and MAPQ = 60
    lecturas_alineadas = 0
    contador_mapq = 0
    
    with open(fichero_sam, 'r') as f:
        for linea in f:
            # We'll ignore the headers that start with "@"
            if not linea.strip() or linea.startswith('@'):
                continue
            # For each of the lines not-ignored, we will add one to the counter lecturas_alineadas
            lecturas_alineadas +=1
            
            # We divide the columns of each line
            columnas = linea.split('\t')
            # We define MAPQ as the fith column 
            mapq  = int(columnas[4])
            # For each time a line has a MAPQ of 60 we add one to the counter contador_mapq
            if mapq == 60:
                contador_mapq +=1

    # We calculate the percentage
    porcentaje = (contador_mapq / lecturas_alineadas) * 100

    # Print the results
    print("Total de lecturas alineadas: ", lecturas_alineadas)
    print("Lecturas con MAPQ = 60: ", contador_mapq)
    print("Porcentaje: ", porcentaje, "%")

if __name__ == "__main__":
    main()
  
