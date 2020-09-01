public class Contractor {
	
	String name;
	String telNum;
	String email;
	String physicalAdd;
	
	public Contractor(String name,String telNum, String email, String physicalAdd)
	{
		this.name = name;
		this.telNum = telNum;
		this.email = email;
		this.physicalAdd = physicalAdd;
	}
	
	public String toString()
	{
	      String output = "Name: " + name;
	      output += "\ntelNum: " + telNum;
	      output += "\nemail: " + email;
	      output += "\nphyasicalAdd: " + physicalAdd;
	      	   
	      return output;
	}
	
	public String getName()
	{
		return name;
	}
}
