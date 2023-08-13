import java.util.Scanner;
public class strong {
 

  private static void myMethod(char [][] cars ) {
    System.out.println(cars[0][0] + "|" + cars[0][1] + "|" + cars[0][2]);
    System.out.println("-----");
    System.out.println(cars[1][0] + "|" + cars[1][1] + "|" + cars[1][2]);
    System.out.println("-----");
    System.out.println(cars[2][0] + "|" + cars[2][1] + "|" + cars[2][2]);
  }

  public static void main(String[] args) {
    char [][] cars = {{' ', ' ', ' '},
     {' ', ' ', ' '}, 
    {' ', ' ', ' '}};

 Scanner scnr = new Scanner(System.in);
    
boolean gameOver = false;


while(!gameOver) {
  System.out.println(" Write the number of space you want to play then enter a space, then X OR O player");
System.out.println();
 myMethod(cars);
   
  String userInput = scnr.nextLine();
   
 int data = userInput.indexOf(" ");


String game = userInput.substring(0,data);
String number = userInput.substring(data+1, userInput.length());

char game2 = game.charAt(0);


System.out.println(number);


 
  switch(number){

    case "1":
cars[0][0] = game2;
 myMethod(cars);
//userInput = scnr.nextLine();
break;
 
case "2":
cars[0][1] = game2;
 myMethod(cars);
// userInput = scnr.nextLine();
break;
 
case "3":
cars[0][2] = game2;
  myMethod(cars);
 // userInput = scnr.nextLine();
break;
 
case "4":
cars[1][0] = game2;
 myMethod(cars);
// userInput = scnr.nextLine();
break;
 
case "5":
cars[1][1] = game2;
  myMethod(cars);
 //userInput = scnr.nextLine();
break;
 
case "6":
cars[1][2] = game2;
  myMethod(cars);
 // userInput = scnr.nextLine();
break;
 
case "7":
cars[2][0] = game2;
 myMethod(cars);
//userInput = scnr.nextLine();
break;

case "8":
cars[2][1] = game2;
 myMethod(cars);
//userInput = scnr.nextLine();
break;
 
case "9":
cars[2][2] = game2;
  myMethod(cars);
  //userInput = scnr.nextLine();
break;
  

  }

  
if(cars[1][0] == game2 && cars[1][1] == game2 && cars[1][2] == game2) {
   if(cars[1][0] == cars[1][1] && cars[1][2] == cars[1][1] && cars[1][0]== cars[1][1])
   {
System.out.println("You won!");
System.exit(0);

    }
  }
 
 else if(cars[0][0] == game2 && cars[0][1] == game2 && cars[0][2] == game2 ) {
  if(cars[0][0] == cars[0][1]&& cars[0][2]== cars[0][1]&& cars[0][2]== cars[0][0]){
    System.out.println("You won!");
System.exit(0);
  }
 }

 else if(cars[2][0] == game2 && cars[2][1] == game2 && cars[2][2] == game2 ) {
  if(cars[2][0] == cars[2][1]&& cars[2][2]== cars[2][1]&& cars[2][2]== cars[2][0]){
    System.out.println("You won!");
System.exit(0);
  }
 }

 else if(cars[0][0] == game2 && cars[1][1] == game2 && cars[2][2] == game2 ) {
  if(cars[0][0] == cars[1][1]&& cars[1][1]== cars[2][2]&& cars[2][2]== cars[0][0]){
    System.out.println("You won!");
System.exit(0);
  }
 }

  else if(cars[0][2] == game2 && cars[1][1] == game2 && cars[2][0] == game2 ) {
  if(cars[0][2] == cars[1][1]&& cars[1][1]== cars[2][0]&& cars[2][0]== cars[0][2]){
    System.out.println("You won!");
System.exit(0);
  }
 }
 
    
    
    

  

 

}
   scnr.close();

  
  }
   
}
