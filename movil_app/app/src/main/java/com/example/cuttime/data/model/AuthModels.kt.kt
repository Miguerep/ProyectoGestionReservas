package com.example.cuttime.data.model

import com.google.gson.annotations.SerializedName

class AuthModels {

    // Petición de Login
    data class LoginRequest(
        val email: String,
        val password: String
    )

    // Respuesta del Login (Token + Usuario)
    data class LoginResponse(
        val msg: String,
        @SerializedName("access_token") val accessToken: String,
        @SerializedName("refresh_token") val refreshToken: String,
        val user: User // Usamos el modelo User que acabamos de crear
    )

    // Petición de Registro (Cliente)
    data class RegistroClienteRequest(
        val nombre: String,
        val apellidos: String,
        val email: String,
        val telefono: String,
        val password: String
    )
}