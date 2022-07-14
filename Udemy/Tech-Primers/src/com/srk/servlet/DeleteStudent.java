<<<<<<< HEAD
package com.srk.servlet;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.srk.dao.StudentDAO;

@WebServlet("/deleteStudent") 
public class DeleteStudent extends HttpServlet {
	protected void doGet(HttpServletRequest request, HttpServletResponse response)   
            throws ServletException, IOException {  
       String sid=request.getParameter("stdId");  
       int id=Integer.parseInt(sid);  
       StudentDAO.deleteStudent(id);  
       response.sendRedirect("viewStudents");  
   }  
}
=======
package com.srk.servlet;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.srk.dao.StudentDAO;

@WebServlet("/deleteStudent") 
public class DeleteStudent extends HttpServlet {
	protected void doGet(HttpServletRequest request, HttpServletResponse response)   
            throws ServletException, IOException {  
       String sid=request.getParameter("stdId");  
       int id=Integer.parseInt(sid);  
       StudentDAO.deleteStudent(id);  
       response.sendRedirect("viewStudents");  
   }  
}
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
