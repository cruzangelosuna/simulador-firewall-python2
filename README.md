
# Simulador de Firewall en Python

## Descripción
Este proyecto consiste en un simulador de filtrado de red mediante un firewall básico programado en Python.

El programa permite o deniega el acceso según la dirección IP de origen, utilizando una lista negra de direcciones bloqueadas.

## Objetivo
Comprender cómo funciona un firewall básico mediante el uso de listas de control de acceso (ACL).

## Herramientas utilizadas
- Python 3
- Programiz Online Compiler
- GitHub

## Funcionamiento
El programa solicita una dirección IP al usuario y verifica si se encuentra dentro de la lista negra.

- Si la IP está bloqueada, muestra ACCESO DENEGADO.
- Si la IP no está bloqueada, muestra ACCESO PERMITIDO.
- Para finalizar el programa se escribe "salir".

## Direcciones IP bloqueadas
- 192.168.1.100
- 10.0.0.25
- 172.16.0.50

## Archivo del proyecto
- simulador_firewall.py

## Autor
Cruz Ángel Martínez Osuna

## Asignatura
Seguridad Informática / Infraestructura de Redes

## Práctica
Práctica 21: Simulación de Filtrado de Red con Firewall.

## Nota
Este programa es una simulación educativa y no bloquea tráfico real de red.
