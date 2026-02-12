package com.example.tuapp.data.model

data class Peluqueria(
    val id: Int,
    val nombre: String,
    val direccion: String,
    val telefono: String,
    val email: String
)

data class Estilista(
    val id: Int,
    val nombre: String,
    val apellidos: String
)