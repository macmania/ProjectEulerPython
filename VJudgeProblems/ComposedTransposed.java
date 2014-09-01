import java.util.Scanner; 

public class ComposedTransposed {
	static String[] NOTESSharp = 
		{"A", "A#", "B", "B#" ,"C", "C#", "D", "D#" , "E", "E#", "F", "F#", "G", "G#"};
	static String[] NOTESFlat = 
		{"Ab", "A", "Bb", "B", "Cb" ,"C", "Db", "D", "Eb" , "E", "Fb", "F", "Gb", "G"};
	
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in); 
		boolean isTranspose; 
		String inputNotes, command; 
		
		while(true){
			
			inputNotes = scan.nextLine();
			
			if(inputNotes.contains("***"))
				break;
			
			command = scan.nextLine();
			
			if(Integer.parseInt(command) == 1){
				isTranspose = true; 
			}
			else {
				isTranspose = false;
			}
			
			transpose(isTranspose, inputNotes);
		}
	}
	
	public static void transpose(boolean cmdTranspose, String notes){
		
		String[] notesArr = notes.split(" ", notes.length());
		String[] outputArr = new String[notesArr.length];
		
		
		for(int i = 0; i < notesArr.length; i++){
			if(notesArr[i].contains("b")){
				int j = 0;
				for(; j < NOTESFlat.length && !NOTESFlat[j].equals(notesArr[i]); j++);
				if(!cmdTranspose ){
					if (j == 0)
						outputArr[i] = NOTESFlat[NOTESFlat.length - 1];
					else
						outputArr[i] = NOTESFlat[j-1];
				}
				else {
					if (j == NOTESFlat.length - 1)
						outputArr[i] = NOTESFlat[0];
					else
						outputArr[i] = NOTESFlat[j+1];
				}
			}
			else {
				int j = 0;
				for(; j < NOTESSharp.length && !NOTESSharp[j].equals(notesArr[i]); j++);
				if(!cmdTranspose){
					if (j == 0)
						outputArr[i] = NOTESSharp[NOTESFlat.length - 1];
					else 
						outputArr[i] = NOTESSharp[j - 1];
				}
				else {
					if (j == NOTESSharp.length - 1)
						outputArr[i] = NOTESSharp[0];
					else 
						outputArr[i] = NOTESSharp[j+1];
				}
			}
		}
		
		for (int j = 0; j < outputArr.length; j++)
			System.out.print(outputArr[j] + ' '); 
		System.out.println(); 
	}
}
