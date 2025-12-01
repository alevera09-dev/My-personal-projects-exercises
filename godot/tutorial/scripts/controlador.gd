extends Node

signal muertes_actualizados

var nivel: int
var muertes: int

func sumar_muertes():
	muertes += 1
	muertes_actualizados.emit()
