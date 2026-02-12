package com.example.tuapp.data.model

import com.google.gson.annotations.SerializedName

// Modelo para recibir citas (GET)
data class Cita(
    val id: Int,
    val fecha: String,
    val estado: String,
    @SerializedName("peluqueria_nombre") val peluqueriaNombre: String?,
    @SerializedName("estilista_nombre") val estilistaNombre: String?,
    val servicios: List<Servicio>
)

// Modelo para enviar una nueva reserva (POST)
data class CitaRequest(
    @SerializedName("peluqueria_id") val peluqueriaId: Int,
    @SerializedName("estilista_id") val estilistaId: Int,
    @SerializedName("servicio_ids") val servicioIds: List<Int>,
    val fecha: String,
    val hora: String
)