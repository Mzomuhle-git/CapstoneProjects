public class Project {
		
		// attributes
		String projectName;
		String projectNum;
		String type;
		String physicalAddress;
		String ERFnum;
		double totFee; 
		double amountPaid;
		String deadline;
		
		public Project(String projectName, String projectNum, String type, String physicalAddress, String ERFnum, double totFee,
				double amountPaid, String deadline)
		{
			this.projectName = projectName;
			this.projectNum = projectNum;
			this.type = type;
			this.physicalAddress = physicalAddress;
			this.ERFnum = ERFnum;
			this.totFee = totFee;
			this.amountPaid = amountPaid;
			this.deadline = deadline;
			
		}
		
		
		public String toString() 
		{
		      String output = "Project Name: " + projectName;
		      output += "\nProject Number: " + projectNum;
		      output += "\nProject Type: " + type;
		      output += "\nPhysical address: " + physicalAddress;
		      output += "\nERF number: " + ERFnum;
		      output += "\nTotal fee: " + totFee;
		      output += "\nAmount paid: " + amountPaid;
		      output += "\nDeadline: " + deadline;
		      	   
		      return output;
		}
		
		
		public String getProjectName()
		{
			return projectName;
		}
		
		
		public String getDuedate()
		{
			
			return deadline;
		}

}
 