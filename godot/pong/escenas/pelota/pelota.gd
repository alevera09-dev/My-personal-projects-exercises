extends CharacterBody2D

@export var area_2d: Area2D
const SPEED := 10.0


func _ready():
	velocity = Vector2(-SPEED, 0)
	connect("body_entered", Callable(self, "_on_body_entered"))

func _physics_process(_delta: float):
	var col: KinematicCollision2D = move_and_collide(velocity)
	
	if col:
		var normal := col.get_normal()
		velocity = velocity.bounce(normal)
	
	
func reset_level():
	get_tree().reload_current_scene()


func _on_area_2d_area_entered(_area: Area2D) -> void:
	print("Choque")
