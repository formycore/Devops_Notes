<<<<<<< HEAD
package com.fullstack.devops.exception;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(value = HttpStatus.NOT_FOUND)
public class RecordNotFoundException extends Exception {

	private static final long serialVersionUID = 1L;
	
	public RecordNotFoundException(String message) {
		super(message);
	}
	
	public RecordNotFoundException(String message, Throwable t) {
		super(message, t);
	}
=======
package com.fullstack.devops.exception;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(value = HttpStatus.NOT_FOUND)
public class RecordNotFoundException extends Exception {

	private static final long serialVersionUID = 1L;
	
	public RecordNotFoundException(String message) {
		super(message);
	}
	
	public RecordNotFoundException(String message, Throwable t) {
		super(message, t);
	}
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
}