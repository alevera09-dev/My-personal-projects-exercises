extends CharacterBody2D

func _physics_process(_delta: float) -> void:

	if Input.is_action_pressed("ui_right"):
		velocity.x += 5
	elif Input.is_action_pressed("ui_left"):
		velocity.x += -5
	else:
		velocity.x = 0

	move_and_slide()
