import javax.swing.*;

public class Swing_JLabel {
    public static void main(String[] args) {
        JFrame f = new JFrame("Creating a label");
        JLabel l1, l2;
        l1 = new JLabel("First Label");
        l2 = new JLabel("Second Label");

        l1.setBounds(50, 50, 100, 30);
        l2.setBounds(50, 100, 100, 30);
        f.add(l1);
        f.add(l2);
        f.setSize(300, 300);
        f.setLayout(null);
        f.setVisible(true);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
