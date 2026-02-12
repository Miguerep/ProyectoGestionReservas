plugins {
    alias(libs.plugins.android.application)
    alias(libs.plugins.kotlin.android)
}

android {
    namespace = "com.example.cuttime"
    compileSdk = 36

    defaultConfig {
        applicationId = "com.example.cuttime"
        minSdk = 26
        targetSdk = 36
        versionCode = 1
        versionName = "1.0"

        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
    }

    buildTypes {
        release {
            isMinifyEnabled = false
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_11
        targetCompatibility = JavaVersion.VERSION_11
    }
    kotlinOptions {
        jvmTarget = "11"
    }
}

dependencies {

    implementation(libs.androidx.core.ktx)
    implementation(libs.androidx.appcompat)
    implementation(libs.material)
    implementation(libs.androidx.activity)
    implementation(libs.androidx.constraintlayout)
    testImplementation(libs.junit)
    androidTestImplementation(libs.androidx.junit)
    androidTestImplementation(libs.androidx.espresso.core)

    // --- 1. RETROFIT (Para conectar con tu API Flask) ---
    implementation("com.squareup.retrofit2:retrofit:2.9.0")

    // Convertidor para transformar el JSON de Flask a objetos Kotlin (Gson)
    implementation("com.squareup.retrofit2:converter-gson:2.9.0")

    // --- 2. OKHTTP (Para ver los logs de las peticiones en consola) ---
    implementation("com.squareup.okhttp3:logging-interceptor:4.11.0")

    // --- 3. CORRUTINAS (Para hacer peticiones sin congelar la app) ---
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-android:1.7.3")

    // --- 4. LIFECYCLE & VIEWMODEL (Para la arquitectura MVVM) ---
    implementation("androidx.lifecycle:lifecycle-viewmodel-ktx:2.6.2")
    implementation("androidx.lifecycle:lifecycle-livedata-ktx:2.6.2")

    // --- 5. SEGURIDAD (Para guardar el Token JWT encriptado) ---
    implementation("androidx.security:security-crypto:1.1.0-alpha06")
}