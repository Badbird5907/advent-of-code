import java.io.File;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class Solution01P1 {
    public static void main(String[] args) {
        File in = new File("input.txt");
        List<Integer> left = new ArrayList<>();
        List<Integer> right = new ArrayList<>();

        try (java.util.Scanner sc = new java.util.Scanner(in)) {
            while (sc.hasNextLine()) {
                // 3   4
                String[] line = sc.nextLine().split(" ");
                left.add(Integer.parseInt(line[0]));
                right.add(Integer.parseInt(line[line.length - 1]));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        left.sort(Comparator.comparingInt(a -> a));
        right.sort(Comparator.comparingInt(a -> a));

        System.out.println(left);
        System.out.println(right);

        if (left.size() != right.size()) {
            throw new RuntimeException("Invalid size!");
        }

        int totalDist = 0;
        for (int i = 0; i < left.size(); i++) {
            int l = left.get(i);
            int r = right.get(i);
            int dist = Math.abs(r - l);
            totalDist += dist;
        }
        System.out.println(totalDist);
    }
}