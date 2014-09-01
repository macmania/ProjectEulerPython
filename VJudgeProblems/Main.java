import java.util.Scanner;

public class Main {
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in); 
		String line; 
		while(true){
			line = scan.nextLine(); 
			
			if (line.equals("0 0 0 0")) 
				break; 
			
			String[] strValues = line.split(" "); 
			
			float sumCalories = Math.round((Integer.parseInt(strValues[0]))/10)*10; 
			float approxCal = Math.round((Integer.parseInt(strValues[1]) * 9 +  
							Integer.parseInt(strValues[2]) * 4 + 
							Integer.parseInt(strValues[3]) * 4)*10)/10;
			
			if(Math.abs(sumCalories  - approxCal) < 10){
				System.out.println("yes");
			}
			else{
				System.out.println("no");
			}
			
		}
	}
}
