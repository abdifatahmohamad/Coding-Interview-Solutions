class Solution {
    public boolean haveConflict(String[] event1, String[] event2) {
        // Convert event strings to integer arrays [startTime, endTime]
        int[] event1Times = convertToMinutes(event1);
        int[] event2Times = convertToMinutes(event2);
        System.out.println("Event1: start= " + event2Times[0] + ", end= " + event2Times[1]);

        // Check if there is any intersection between the two events
        if (event1Times[0] <= event2Times[1] && event2Times[0] <= event1Times[1]) {
            // Intersection exists, return true
            return true;
        } else {
            // No intersection, return false
            return false;
        }
    }

    private int[] convertToMinutes(String[] event) {
        int[] times = new int[2];
        for (int i = 0; i < 2; i++) {
            // Split the time string into hours and minutes
            String[] parts = event[i].split(":"); 
             // Extract the hours part and convert it to an integer
            int hours = Integer.parseInt(parts[0]); 
            // Extract the minutes part and convert it to an integer
            int minutes = Integer.parseInt(parts[1]);  
            // Convert hours to minutes and add them to the minutes
            times[i] = hours * 60 + minutes;  
        }
        return times;  // Return the array [startTime, endTime]
    }
}