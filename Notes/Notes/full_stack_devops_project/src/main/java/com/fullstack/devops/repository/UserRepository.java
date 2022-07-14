<<<<<<< HEAD
package com.fullstack.devops.repository;

import java.util.List;

import org.springframework.data.repository.CrudRepository;

import com.fullstack.devops.model.User;


public interface UserRepository extends CrudRepository<User, Long> {
	List<User> findByFirstname(String firstname);
}
=======
package com.fullstack.devops.repository;

import java.util.List;

import org.springframework.data.repository.CrudRepository;

import com.fullstack.devops.model.User;


public interface UserRepository extends CrudRepository<User, Long> {
	List<User> findByFirstname(String firstname);
}
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
