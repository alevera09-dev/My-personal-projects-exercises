extends CharacterBody2D


const SPEED = 500.0


func _physics_process(_delta: float) -> void:

	# Handle jump.
	if Input.is_action_pressed("up"):
		velocity.y = -SPEED
	
	elif Input.is_action_pressed("down"):
		velocity.y = SPEED
	
	else:
		velocity.y = 0
		
	move_and_slide()
