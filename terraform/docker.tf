terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.13"
    }
  }
}

# Configura el proveedor de Docker
# Si estás usando Docker Desktop en Windows, Terraform debería 
# conectarse automáticamente al daemon de Docker sin necesidad 
# de especificar un host.
provider "docker" {}

# Define un recurso de imagen de Docker para NGINX
resource "docker_image" "nginx" {
  name         = "nginx:latest"
  keep_locally = false # Esto asegura que la imagen se descargue si no está localmente
}

# Crea un contenedor Docker usando la imagen de NGINX
resource "docker_container" "nginx_container" {
  image = docker_image.nginx.latest
  name  = "nginx-container"
  ports {
    internal = 80
    external = 5052
  }
}
