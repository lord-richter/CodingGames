import java.util.*;
import java.io.*;
import java.math.*;


/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/ 
class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int nbFloors = in.nextInt(); // number of floors
        int width = in.nextInt(); // width of the area
        int nbRounds = in.nextInt(); // maximum number of rounds
        int exitFloor = in.nextInt(); // floor on which the exit is found
        int exitPos = in.nextInt(); // position of the exit on its floor
        int nbTotalClones = in.nextInt(); // number of generated clones
        int nbAdditionalElevators = in.nextInt(); // ignore (always zero)
        int nbElevators = in.nextInt(); // number of elevators

        // store all elevators for easy reference
        HashMap<Integer,Integer> elevatorList = new HashMap<Integer,Integer>();

        // keep track of our blocked clones
        HashMap<Integer,Integer> blockedClones = new HashMap<Integer,Integer>();

        for (int i = 0; i < nbElevators; i++) {
            int elevatorFloor = in.nextInt(); // floor on which this elevator is found
            int elevatorPos = in.nextInt(); // position of the elevator on its floor
            elevatorList.put(elevatorFloor,elevatorPos);
        }

        // game loop
        while (true) {
            int cloneFloor = in.nextInt(); // floor of the leading clone
            int clonePos = in.nextInt(); // position of the leading clone on its floor
            String direction = in.next(); // direction of the leading clone: LEFT or RIGHT

            // default action is to wait.
            String action = "WAIT";

            // summary
            // as long as the leading clone is heading to an elevator,
            // or heading to another clone, we WAIT.  

            // can assume only one elevator per floor

            // are they heading to an elevator?
            // distance to next elevator (+ to the right, - to the left)
            int nearestElevator = (elevatorList.containsKey(cloneFloor)?elevatorList.get(cloneFloor) - clonePos:0);
            // if they are standing on the elevator...
            // if they are moving left and the elevator is to the left...
            // if they are moving right and the elevator is to the right...
            // if there is one floor and there are no elevators...
            // then there is no need to stop them...
            boolean movingToElevator = (nearestElevator==0 | (direction.compareToIgnoreCase("LEFT")==0 && nearestElevator<0) | (direction.compareToIgnoreCase("RIGHT")==0 && nearestElevator>0));

            // are they heading to a clone?
            // we only need one clone per floor, for the purpose of turning the
            // active clone around.  Once turned around, they should be heading
            // to an elevator
            boolean movingToClone = false;
            int nearestClone = 99999;
            if (blockedClones.containsKey(cloneFloor)) {
                // distance to clone (+ to the right, - to the left)
                nearestClone = blockedClones.get(cloneFloor) - clonePos;
                movingToClone = ((direction.compareToIgnoreCase("LEFT")==0 && nearestClone<0) | (direction.compareToIgnoreCase("RIGHT")==0 && nearestClone>0));
            }

            // are they on the exit floor?
            boolean onExitFloor = cloneFloor==exitFloor;

            // assuming they are, how far are they from the exit?
            // distance to exit (+ to the right, - to the left)
            int nearestExit = exitPos - clonePos;

            // if we are on the exit floor, we need to know if they are moving
            // towards the exit
            // this is TRUE when we are on the exit floor the exit is in the direction 
            // of movement.
            boolean movingToExit = onExitFloor && ((direction.compareToIgnoreCase("LEFT")==0 && nearestExit<0) | (direction.compareToIgnoreCase("RIGHT")==0 && nearestExit>0));

            System.err.printf("Elevator: %b,   Clone: %b     Exit:%b",movingToElevator,movingToClone,movingToExit);

            // if we are moving towards the elevator, or there is no elevator, then WAIT
            // if we are not moving towards the elevator, but towards a clone, then WAIT
            // if we are on the exit floor, and moving towards the exit, then WAIT

            // determine if we need to BLOCK
            if (onExitFloor && !movingToExit) { 
                action = "BLOCK";
            } else if (!movingToClone && !movingToElevator) {
                action = "BLOCK";
            } 

            System.out.println(action); // action: WAIT or BLOCK
        }
    }
}