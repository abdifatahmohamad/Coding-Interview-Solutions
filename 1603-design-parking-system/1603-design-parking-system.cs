public class ParkingSystem {
    private int bigSlots;
    private int mediumSlots;
    private int smallSlots;

    public ParkingSystem(int big, int medium, int small) {
        
        bigSlots = big;
        mediumSlots = medium;
        smallSlots = small;
        
    }
    
    public bool AddCar(int carType) {
        
        switch(carType){
                
            case 1:
                if(bigSlots > 0){
                    bigSlots--;
                    return true;
                }
                break;
                
            case 2:
                if(mediumSlots > 0){
                    mediumSlots--;
                    return true;
                }
                break;
            case 3:
                if(smallSlots > 0){
                    smallSlots--;
                    return true;
                }
                break;
                
        }
        
        return false;
        
        // Check whether there is parking space of carType
        
        // CarType can be of three kinds 1, 2, 3 respectively
        
        // Car can only park in a parking space of its carType, return true if space available, else false
        
        
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj.AddCar(carType);
 */