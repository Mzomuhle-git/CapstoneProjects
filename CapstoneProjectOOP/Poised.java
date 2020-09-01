 import java.util.Scanner;

public class Poised {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		String projectName = null;
		String projectNum = null;
		String type = null;
		String physicalAddress = null;
		String ERFnum = null;
		double totFee = 0; 
		double amountPaid = 0;
		String deadline = null;
		
		String contractorName = null;
		String contractorNum = null;
		String contractorEmail = null;
		String contractorPhysicalAddress = null;
		
		System.out.println("Welcome to poised online System \nSelect an option to continue");
		System.out.println("1 - To enter new project\n2 - To capture the Contractor contacts: ");
		int option = input.nextInt();
		input.nextLine();
		
		if(option == 1){
	
			System.out.print("Enter Project name: ");
			projectName = input.nextLine();
			System.out.print("Enter Project number: ");
			projectNum = input.nextLine();
			System.out.print("Enter the project type: ");
			type = input.nextLine();
			System.out.print("Physical Address: ");
			physicalAddress = input.nextLine();
			System.out.print("ERF number: ");
			ERFnum = input.nextLine();
			System.out.print("Total fee: ");
			totFee = input.nextDouble();
			System.out.print("Amount paid: ");
			amountPaid = input.nextDouble();
			System.out.print("Deadline: ");
			deadline = input.next();
			
			Project project = new Project(projectName, projectNum, type, physicalAddress, ERFnum, totFee, amountPaid, deadline);
			System.out.println("\n\nYour project has been created\n");
			System.out.print(project);
		}
		else if (option == 2){
		
			System.out.print("Enter Contractor name: ");
			contractorName = input.nextLine();
			System.out.print("Enter telephone number: ");
			contractorNum = input.nextLine();
			System.out.print("Email address: ");
			contractorEmail = input.nextLine();
			System.out.print("Physical Address: ");
			contractorPhysicalAddress = input.nextLine();
			
			Contractor contractor = new Contractor(contractorName, contractorNum, contractorEmail, contractorPhysicalAddress);
			System.out.println("\n\nContractor details captured\n");
			System.out.println(contractor);
			}
				
		
	    input.close();

	}
}
