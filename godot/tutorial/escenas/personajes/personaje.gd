extends CharacterBody2D

signal personaje_muerto

@export var animacion: Node
@export var area_2d: Node
@export var material_personaje_rojo: ShaderMaterial

var _velocidad: float = 100.0
var _velocidad_de_salto: float = -350.0
var _muerto: bool


func _ready() -> void:
	area_2d.body_entered.connect(_on_area_2d_body_entered)
	add_to_group("personajes")
	
func _physics_process(delta):
	if _muerto:
		return
		
	#gravedad
	velocity += get_gravity() * delta
	

	#salto
	if Input.is_action_just_pressed("saltar") and is_on_floor():
		velocity.y = _velocidad_de_salto
		
	#Movimiento lateral
	if Input.is_action_pressed("derecha"):
		animacion.flip_h = true
		velocity.x = _velocidad
	elif Input.is_action_pressed("izquierda"):
		animacion.flip_h = false
		velocity.x = -_velocidad
		
	else:
		velocity.x = 0
		animacion.play("idle")
		
	move_and_slide()
	
	#animacion
	if !is_on_floor():
		animacion.play("saltar")
	elif velocity.x != 0:
		animacion.play("correr")
	else:
		animacion.play("idle")


func _on_area_2d_body_entered(_body: Node2D) -> void:
	_muerto = true
	animacion.material = material_personaje_rojo
	animacion.stop()
	
	await get_tree().create_timer(0.5).timeout
	personaje_muerto.emit()

	ControladorGlobal.sumar_muertes()
