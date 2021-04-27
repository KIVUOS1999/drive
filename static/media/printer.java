package q2;

public class printer {
	synchronized public void print(int work_id)
	{
		for(int i=0; i<5; i++)
		{
			try {
				Thread.sleep(1000);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			
			System.out.println("work id: "+work_id + "page: "+ (i+1));
		}
	}
}
