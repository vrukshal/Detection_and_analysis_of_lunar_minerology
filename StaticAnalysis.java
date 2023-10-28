/* Java program for Static Analysis.*/


public class StaticAnalysis
{
    public static void main(String[] args)
    {
        calculateCost(5, 10, "Electronics");
        String value =  calculateCost(2, 3, "Clothing");
        System.out.println(value);
    }

    public StaticAnalysis()
    {
        int weight = 0;
        String length = "";
    }

    public static String calculateCost(int weight, int length, String product)
    {
        int cost = 0;
        String output = "";

        if(product == "Electronics")
        {
            cost = weight * length * 2;
        }
        else
        {
            cost = weight * length;
        }

        if(cost < 15)
            output = "Your product costs a flat rate of $10.00 to ship.";
        else
            output = "Your product costs $" + Integer.toString(cost) + " to ship.";

        return output;

    }
}