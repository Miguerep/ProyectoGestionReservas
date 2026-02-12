package com.example.tuapp.data.model

data class Servicio(
    val id: Int,
    val nombre: String,
    val descripcion: String?,
    val precio: Double,
    val duracion: Int
) {
    // mostrar el nombre y precio en listas (UI)
    override fun toString(): String {
        return "$nombre - ${precio}€"
    }
}