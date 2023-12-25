try{
    console.log(hsr); // Error: hsr is not defined
} catch(error){
    console.log("Error Name :", error.name);
    console.log("Error Message :", error.message);
}