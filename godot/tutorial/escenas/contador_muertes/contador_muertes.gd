extends Control

@export var label: Label

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	ControladorGlobal.muertes_actualizados.connect(_actualizar_text)
	_actualizar_text()

func _actualizar_text():
	label.text = str(ControladorGlobal.muertes)
