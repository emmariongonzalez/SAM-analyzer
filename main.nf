// Definimos el parametro sam con la ruta donde se encuentra el archivo
params.sam = "/path/to/your/file.sam"

workflow {
    // Comprovamos que en el comando tengamos un archivo
    if (params.sam == "") {
        error "ERROR: Debes proporcionar un archivo SAM"
    }

    // Creamos un canal
    sam_file_ch = Channel.fromPath(params.sam)

    // Ejecutamos el proceso de análisis
    ANALYZE_SAM(sam_file_ch)
}

// Definimos el proceso de analisis del archivo
process ANALYZE_SAM {
    debug true

    input:
    path sam_input

    script:
    """
    # Utilizaremos el script de python mediante uv
    uv run main.py ${sam_input}
    """
}
