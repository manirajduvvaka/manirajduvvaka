import java.util.Scanner;

public class OnlineExamination 
    public static void main(String[] args) {
        String[] questions = {
            "What is the capital of France?",
            "Which planet is known as the Red Planet?",
            "What is the largest mammal in the world?"
        };

        String[] options = {
            "A) Paris B) Rome C) Madrid D) London",
            "A) Mars B) Venus C) Earth D) Jupiter",
            "A) Elephant B) Blue Whale C) Giraffe D) Polar Bear"
        };

        char[] answers = {'A', 'A', 'B'};
        int score = 0;
        Scanner scanner = new Scanner(System.in);
        for (int i = 0; i < questions.length; i++) {
            System.out.println("Question " + (i + 1) + ": " + questions[i]);
            System.out.println(options[i]);
            System.out.print("Your answer: ");
            char userAnswer = scanner.next().toUpperCase().charAt(0);
            if (userAnswer == answers[i]) {
                System.out.println("Correct!");
                score++;
            } else {
                System.out.println("Incorrect!");
            }
            System.out.println();
        }
        System.out.println("Your score: " + score + "/" + questions.length);
        scanner.close();
    }
}
