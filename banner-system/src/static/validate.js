function validate()
{ 
   if(document.StudentRegistration.firstName.value == "")
   {
     alert( "Please provide your First Name!" );
     document.StudentRegistration.firstName.focus() ;
     return false;
   }
   if(document.StudentRegistration.lastName.value == "")
   {
     alert( "Please provide your Last Name!" );
     document.StudentRegistration.lastName.focus() ;
     return false;
   }
   if(document.StudentRegistration.address.value == "")
   {
     alert( "Please provide your Address!" );
     document.StudentRegistration.address.focus() ;
     return false;
   }
   if(document.StudentRegistration.city.value == "")
   {
     alert( "Please provide your City!" );
     document.StudentRegistration.city.focus() ;
     return false;
   }    
   if((document.StudentRegistration.state.value == ""))
   {
     alert( "Please provide your State!" ); 
     document.StudentRegistration.state.focus() ;

     return false;
   }
   if( document.StudentRegistration.zipcode.value == "" ||
           isNaN( document.StudentRegistration.zipcode.value) ||
           document.StudentRegistration.zipcode.value.length != 5 )
   {
     alert( "Please provide a zipcode in the format ######." );
     document.StudentRegistration.zipcode.focus() ;
     return false;
   }
   if(document.StudentRegistration.country.value == "" )
   {
     alert( "Please provide your Country!" ); 
     document.StudentRegistration.country.focus() ;
     return false;
   	}
   	var email = document.StudentRegistration.emailid.value;
 	atpos = email.indexOf("@");
  	dotpos = email.lastIndexOf(".");
	if(email == "" || atpos < 1 || ( dotpos - atpos < 2 )) 
 	{
     	alert("Please enter correct email ID")
     	document.StudentRegistration.emailid.focus() ;
     	return false;
 	}
 	if(document.StudentRegistration.mobileno.value == "" ||
           isNaN( document.StudentRegistration.mobileno.value) ||
           document.StudentRegistration.mobileno.value.length != 10 )
   	{
    	alert("Please provide a Mobile No in the format 123.");
     	document.StudentRegistration.mobileno.focus() ;
     	return false;
   	}
   if(document.StudentRegistration.sex.value == "-1")
   {
     alert( "Please chose an option!" );
     document.StudentRegistration.sex.focus() ;
     return false;
   }   
   if(document.StudentRegistration.banner.value == "" ||
           isNaN( document.StudentRegistration.banner.value) ||
           document.StudentRegistration.banner.value.length != 9 )
   {
     alert( "Please provide a pincode in the format ######." );
     document.StudentRegistration.banner.focus() ;
     return false;
   }
 
 
  if(document.StudentRegistration.dob.value == "")
   {
     alert( "Please provide your DOB!" );
     document.StudentRegistration.dob.focus() ;
     return false;
   }
 
   return( true );
}