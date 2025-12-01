extends Node2D

@export var area_2d: Area2D
@export var reproductor: AudioStreamPlayer2D


var contenedor_monedas: ContenedorMonedas

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	area_2d.body_entered.connect(_recogida)
	
	
func _recogida(_body):
	contenedor_monedas.moneda_recogida()
	reproductor.reparent(get_parent().get_parent().get_parent())
	reproductor.play()
	queue_free()
