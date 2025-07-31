import java.util.Scanner;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Random rand = new Random();

        int score = 0;
        boolean playAgain = true;

        System.out.println("🎯 Welcome to the Number Game!");

        while (playAgain) {
            int target = rand.nextInt(100) + 1;  // random number from 1 to 100
            int attempts = 0;
            boolean guessedCorrectly = false;

            System.out.println("\n🔢 I have picked a number between 1 and 100.");
            System.out.println("🧠 Try to guess it! You have 7 attempts.");

            while (attempts < 7) {
                System.out.print("👉 Enter your guess: ");
                int guess = input.nextInt();
                attempts++;

                if (guess == target) {
                    System.out.println("✅ Correct! You guessed it in " + attempts + " attempts.");
                    score++;
                    guessedCorrectly = true;
                    break;
                } else if (guess < target) {
                    System.out.println("⬆️ Too low! Try again.");
                } else {
                    System.out.println("⬇️ Too high! Try again.");
                }
            }

            if (!guessedCorrectly) {
                System.out.println("❌ You've used all attempts! The number was: " + target);
            }

            System.out.print("\n🔁 Do you want to play again? (yes/no): ");
            String response = input.next().toLowerCase();
            playAgain = response.equals("yes");
        }

        System.out.println("\n🏁 Game Over! Your total score: " + score);
        input.close();
    }
}